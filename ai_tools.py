"""AI tools for the Shipping module."""
from assistant.tools import AssistantTool, register_tool


@register_tool
class ListShipments(AssistantTool):
    name = "list_shipments"
    description = "List shipments with optional status filter."
    module_id = "shipping"
    required_permission = "shipping.view_shipment"
    parameters = {
        "type": "object",
        "properties": {
            "status": {"type": "string", "description": "Filter: pending, picked, in_transit, delivered, returned"},
            "limit": {"type": "integer", "description": "Max results (default 20)"},
        },
        "required": [],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from shipping.models import Shipment
        qs = Shipment.objects.select_related('carrier').order_by('-ship_date')
        if args.get('status'):
            qs = qs.filter(status=args['status'])
        limit = args.get('limit', 20)
        return {
            "shipments": [
                {
                    "id": str(s.id),
                    "reference": s.reference,
                    "carrier": s.carrier.name if s.carrier else None,
                    "tracking_number": s.tracking_number,
                    "status": s.status,
                    "recipient_name": s.recipient_name,
                    "ship_date": str(s.ship_date) if s.ship_date else None,
                    "delivery_date": str(s.delivery_date) if s.delivery_date else None,
                }
                for s in qs[:limit]
            ],
            "total": qs.count(),
        }


@register_tool
class CreateShipment(AssistantTool):
    name = "create_shipment"
    description = "Create a new shipment."
    module_id = "shipping"
    required_permission = "shipping.change_shipment"
    requires_confirmation = True
    parameters = {
        "type": "object",
        "properties": {
            "carrier_id": {"type": "string", "description": "Carrier ID"},
            "recipient_name": {"type": "string", "description": "Recipient name"},
            "recipient_address": {"type": "string", "description": "Recipient address"},
            "tracking_number": {"type": "string", "description": "Tracking number"},
            "notes": {"type": "string", "description": "Shipping notes"},
        },
        "required": ["recipient_name", "recipient_address"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from datetime import date
        from shipping.models import Shipment
        s = Shipment.objects.create(
            carrier_id=args.get('carrier_id'),
            recipient_name=args['recipient_name'],
            recipient_address=args['recipient_address'],
            tracking_number=args.get('tracking_number', ''),
            notes=args.get('notes', ''),
            ship_date=date.today(),
            status='pending',
        )
        return {"id": str(s.id), "reference": s.reference, "created": True}
