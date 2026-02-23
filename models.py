from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.base import HubBaseModel

SHIP_STATUS = [
    ('pending', _('Pending')),
    ('picked', _('Picked Up')),
    ('in_transit', _('In Transit')),
    ('delivered', _('Delivered')),
    ('returned', _('Returned')),
]

class Carrier(HubBaseModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    code = models.CharField(max_length=50, blank=True, verbose_name=_('Code'))
    tracking_url = models.URLField(blank=True, verbose_name=_('Tracking Url'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))

    class Meta(HubBaseModel.Meta):
        db_table = 'shipping_carrier'

    def __str__(self):
        return self.name


class Shipment(HubBaseModel):
    reference = models.CharField(max_length=50, verbose_name=_('Reference'))
    carrier = models.ForeignKey('Carrier', on_delete=models.SET_NULL, null=True)
    tracking_number = models.CharField(max_length=100, blank=True, verbose_name=_('Tracking Number'))
    status = models.CharField(max_length=20, default='pending', choices=SHIP_STATUS, verbose_name=_('Status'))
    ship_date = models.DateField(null=True, blank=True, verbose_name=_('Ship Date'))
    delivery_date = models.DateField(null=True, blank=True, verbose_name=_('Delivery Date'))
    recipient_name = models.CharField(max_length=255, verbose_name=_('Recipient Name'))
    recipient_address = models.TextField(verbose_name=_('Recipient Address'))
    weight = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name=_('Weight'))
    notes = models.TextField(blank=True, verbose_name=_('Notes'))

    class Meta(HubBaseModel.Meta):
        db_table = 'shipping_shipment'

    def __str__(self):
        return self.reference

