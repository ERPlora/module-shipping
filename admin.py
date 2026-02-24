from django.contrib import admin

from .models import Carrier, Shipment

@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'tracking_url', 'is_active', 'created_at']
    search_fields = ['name', 'code']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['reference', 'carrier', 'tracking_number', 'status', 'ship_date', 'created_at']
    search_fields = ['reference', 'tracking_number', 'status', 'recipient_name']
    readonly_fields = ['created_at', 'updated_at']

