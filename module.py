from django.utils.translation import gettext_lazy as _

MODULE_ID = 'shipping'
MODULE_NAME = _('Shipping & Delivery')
MODULE_VERSION = '1.0.0'
MODULE_ICON = 'car-outline'
MODULE_DESCRIPTION = _('Shipping management, carriers and tracking')
MODULE_AUTHOR = 'ERPlora'
MODULE_CATEGORY = 'commerce'

MENU = {
    'label': _('Shipping & Delivery'),
    'icon': 'car-outline',
    'order': 20,
}

NAVIGATION = [
    {'label': _('Dashboard'), 'icon': 'speedometer-outline', 'id': 'dashboard'},
{'label': _('Shipments'), 'icon': 'car-outline', 'id': 'shipments'},
{'label': _('Carriers'), 'icon': 'bus-outline', 'id': 'carriers'},
{'label': _('Settings'), 'icon': 'settings-outline', 'id': 'settings'},
]

DEPENDENCIES = []

PERMISSIONS = [
    'shipping.view_shipment',
'shipping.add_shipment',
'shipping.change_shipment',
'shipping.delete_shipment',
'shipping.view_carrier',
'shipping.add_carrier',
'shipping.change_carrier',
'shipping.manage_settings',
]
