from django.contrib import admin

from .models import Carrier, Shipment

@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'tracking_url', 'is_active']
    readonly_fields = ['id', 'hub_id', 'created_at', 'updated_at']
    ordering = ['-created_at']


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['reference', 'carrier', 'tracking_number', 'status', 'ship_date']
    readonly_fields = ['id', 'hub_id', 'created_at', 'updated_at']
    ordering = ['-created_at']

