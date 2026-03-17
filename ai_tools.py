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


@register_tool
class UpdateShipment(AssistantTool):
    name = "update_shipment"
    description = "Update a shipment's fields (carrier, tracking, status, dates, recipient, weight, notes)."
    module_id = "shipping"
    required_permission = "shipping.change_shipment"
    requires_confirmation = True
    parameters = {
        "type": "object",
        "properties": {
            "shipment_id": {"type": "string", "description": "Shipment ID"},
            "carrier_id": {"type": "string"},
            "tracking_number": {"type": "string"},
            "status": {"type": "string", "description": "pending, picked, in_transit, delivered, returned"},
            "ship_date": {"type": "string", "description": "Date (YYYY-MM-DD)"},
            "delivery_date": {"type": "string", "description": "Date (YYYY-MM-DD)"},
            "recipient_name": {"type": "string"},
            "recipient_address": {"type": "string"},
            "weight": {"type": "string", "description": "Weight in kg"},
            "notes": {"type": "string"},
        },
        "required": ["shipment_id"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from decimal import Decimal
        from shipping.models import Shipment
        try:
            s = Shipment.objects.get(id=args['shipment_id'])
        except Shipment.DoesNotExist:
            return {"error": f"Shipment {args['shipment_id']} not found"}
        fields = ['updated_at']
        for field in ('tracking_number', 'status', 'ship_date', 'delivery_date',
                      'recipient_name', 'recipient_address', 'notes'):
            if field in args:
                setattr(s, field, args[field])
                fields.append(field)
        if 'carrier_id' in args:
            s.carrier_id = args['carrier_id']
            fields.append('carrier_id')
        if 'weight' in args:
            s.weight = Decimal(args['weight']) if args['weight'] else None
            fields.append('weight')
        s.save(update_fields=fields)
        return {"id": str(s.id), "reference": s.reference, "updated": True}


@register_tool
class DeleteShipment(AssistantTool):
    name = "delete_shipment"
    description = "Delete a shipment by ID."
    module_id = "shipping"
    required_permission = "shipping.change_shipment"
    requires_confirmation = True
    parameters = {
        "type": "object",
        "properties": {
            "shipment_id": {"type": "string", "description": "Shipment ID"},
        },
        "required": ["shipment_id"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from shipping.models import Shipment
        try:
            s = Shipment.objects.get(id=args['shipment_id'])
            reference = s.reference
            s.delete()
            return {"deleted": True, "reference": reference}
        except Shipment.DoesNotExist:
            return {"error": f"Shipment {args['shipment_id']} not found"}
