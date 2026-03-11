"""
AI context for the Shipping module.
Loaded into the assistant system prompt when this module's tools are active.
"""

CONTEXT = """
## Module Knowledge: Shipping

### Models

**Carrier**
- `name` (str, required), `code` (str, optional), `tracking_url` (URL, optional), `is_active` (bool)
- Represents a shipping carrier (e.g. DHL, FedEx, Correos).
- `tracking_url` can be used as a template for building tracking links.

**Shipment**
- `reference` (str, required), `carrier` (FK → Carrier, SET_NULL, nullable)
- `tracking_number` (str, optional), `status` choices: pending | picked | in_transit | delivered | returned
- `ship_date` (date, optional), `delivery_date` (date, optional)
- `recipient_name` (str, required), `recipient_address` (text, required)
- `weight` (decimal kg, optional), `notes` (text)

### Key Flows

1. **Create carrier**: provide name, optional code and tracking_url.
2. **Create shipment**: set reference, recipient info (name + address), link carrier, optionally set tracking_number.
3. **Progress status**: pending → picked → in_transit → delivered. If returned, set status to 'returned'.
4. **Record dates**: set ship_date when dispatched, delivery_date when confirmed delivered.

### Relationships

- Shipment → Carrier (SET_NULL on delete; a shipment can exist without a carrier).
- No direct FK to orders or customers in this module — reference field is used to link externally.
"""
