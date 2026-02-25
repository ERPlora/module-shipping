# Shipping & Delivery Module

Shipping management, carriers and tracking.

## Features

- Manage shipping carriers with tracking URL templates
- Create and track shipments through their full lifecycle (pending, picked up, in transit, delivered, returned)
- Record tracking numbers, ship dates, and delivery dates
- Store recipient details including name, address, and package weight
- Dashboard with shipment overview and status metrics

## Installation

This module is installed automatically via the ERPlora Marketplace.

## Configuration

Access settings via: **Menu > Shipping & Delivery > Settings**

## Usage

Access via: **Menu > Shipping & Delivery**

### Views

| View | URL | Description |
|------|-----|-------------|
| Dashboard | `/m/shipping/dashboard/` | Shipment overview and key metrics |
| Shipments | `/m/shipping/shipments/` | List, create and manage shipments |
| Carriers | `/m/shipping/carriers/` | Manage shipping carriers and tracking URLs |
| Settings | `/m/shipping/settings/` | Module configuration |

## Models

| Model | Description |
|-------|-------------|
| `Carrier` | Shipping carrier with name, code, tracking URL template, and active status |
| `Shipment` | Individual shipment with reference, carrier link, tracking number, status, dates, recipient info, weight, and notes |

## Permissions

| Permission | Description |
|------------|-------------|
| `shipping.view_shipment` | View shipments |
| `shipping.add_shipment` | Create new shipments |
| `shipping.change_shipment` | Edit existing shipments |
| `shipping.delete_shipment` | Delete shipments |
| `shipping.view_carrier` | View carriers |
| `shipping.add_carrier` | Create new carriers |
| `shipping.change_carrier` | Edit existing carriers |
| `shipping.manage_settings` | Manage module settings |

## License

MIT

## Author

ERPlora Team - support@erplora.com
