# Shipping & Delivery

## Overview

| Property | Value |
|----------|-------|
| **Module ID** | `shipping` |
| **Version** | `1.0.0` |
| **Icon** | `car-outline` |
| **Dependencies** | None |

## Models

### `Carrier`

Carrier(id, hub_id, created_at, updated_at, created_by, updated_by, is_deleted, deleted_at, name, code, tracking_url, is_active)

| Field | Type | Details |
|-------|------|---------|
| `name` | CharField | max_length=255 |
| `code` | CharField | max_length=50, optional |
| `tracking_url` | URLField | max_length=200, optional |
| `is_active` | BooleanField |  |

### `Shipment`

Shipment(id, hub_id, created_at, updated_at, created_by, updated_by, is_deleted, deleted_at, reference, carrier, tracking_number, status, ship_date, delivery_date, recipient_name, recipient_address, weight, notes)

| Field | Type | Details |
|-------|------|---------|
| `reference` | CharField | max_length=50 |
| `carrier` | ForeignKey | → `shipping.Carrier`, on_delete=SET_NULL, optional |
| `tracking_number` | CharField | max_length=100, optional |
| `status` | CharField | max_length=20, choices: pending, picked, in_transit, delivered, returned |
| `ship_date` | DateField | optional |
| `delivery_date` | DateField | optional |
| `recipient_name` | CharField | max_length=255 |
| `recipient_address` | TextField |  |
| `weight` | DecimalField | optional |
| `notes` | TextField | optional |

## Cross-Module Relationships

| From | Field | To | on_delete | Nullable |
|------|-------|----|-----------|----------|
| `Shipment` | `carrier` | `shipping.Carrier` | SET_NULL | Yes |

## URL Endpoints

Base path: `/m/shipping/`

| Path | Name | Method |
|------|------|--------|
| `(root)` | `dashboard` | GET |
| `shipments/` | `shipments` | GET |
| `carriers/` | `carriers_list` | GET |
| `carriers/add/` | `carrier_add` | GET/POST |
| `carriers/<uuid:pk>/edit/` | `carrier_edit` | GET |
| `carriers/<uuid:pk>/delete/` | `carrier_delete` | GET/POST |
| `carriers/<uuid:pk>/toggle/` | `carrier_toggle_status` | GET |
| `carriers/bulk/` | `carriers_bulk_action` | GET/POST |
| `settings/` | `settings` | GET |

## Permissions

| Permission | Description |
|------------|-------------|
| `shipping.view_shipment` | View Shipment |
| `shipping.add_shipment` | Add Shipment |
| `shipping.change_shipment` | Change Shipment |
| `shipping.delete_shipment` | Delete Shipment |
| `shipping.view_carrier` | View Carrier |
| `shipping.add_carrier` | Add Carrier |
| `shipping.change_carrier` | Change Carrier |
| `shipping.manage_settings` | Manage Settings |

**Role assignments:**

- **admin**: All permissions
- **manager**: `add_carrier`, `add_shipment`, `change_carrier`, `change_shipment`, `view_carrier`, `view_shipment`
- **employee**: `add_shipment`, `view_carrier`, `view_shipment`

## Navigation

| View | Icon | ID | Fullpage |
|------|------|----|----------|
| Dashboard | `speedometer-outline` | `dashboard` | No |
| Shipments | `car-outline` | `shipments` | No |
| Carriers | `bus-outline` | `carriers` | No |
| Settings | `settings-outline` | `settings` | No |

## AI Tools

Tools available for the AI assistant:

### `list_shipments`

List shipments with optional status filter.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `status` | string | No | Filter: pending, picked, in_transit, delivered, returned |
| `limit` | integer | No | Max results (default 20) |

### `create_shipment`

Create a new shipment.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `carrier_id` | string | No | Carrier ID |
| `recipient_name` | string | Yes | Recipient name |
| `recipient_address` | string | Yes | Recipient address |
| `tracking_number` | string | No | Tracking number |
| `notes` | string | No | Shipping notes |

## File Structure

```
README.md
__init__.py
admin.py
ai_tools.py
apps.py
forms.py
locale/
  en/
    LC_MESSAGES/
      django.po
  es/
    LC_MESSAGES/
      django.po
migrations/
  0001_initial.py
  __init__.py
models.py
module.py
static/
  icons/
    icon.svg
  shipping/
    css/
    js/
templates/
  shipping/
    pages/
      carrier_add.html
      carrier_edit.html
      carriers.html
      dashboard.html
      index.html
      settings.html
      shipments.html
    partials/
      carrier_add_content.html
      carrier_edit_content.html
      carriers_content.html
      carriers_list.html
      dashboard_content.html
      panel_carrier_add.html
      panel_carrier_edit.html
      settings_content.html
      shipments_content.html
tests/
  __init__.py
  conftest.py
  test_models.py
  test_views.py
urls.py
views.py
```
