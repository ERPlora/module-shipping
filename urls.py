from django.urls import path
from . import views

app_name = 'shipping'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Navigation tab aliases
    path('shipments/', views.dashboard, name='shipments'),


    # Carrier
    path('carriers/', views.carriers_list, name='carriers_list'),
    path('carriers/add/', views.carrier_add, name='carrier_add'),
    path('carriers/<uuid:pk>/edit/', views.carrier_edit, name='carrier_edit'),
    path('carriers/<uuid:pk>/delete/', views.carrier_delete, name='carrier_delete'),
    path('carriers/<uuid:pk>/toggle/', views.carrier_toggle_status, name='carrier_toggle_status'),
    path('carriers/bulk/', views.carriers_bulk_action, name='carriers_bulk_action'),

    # Settings
    path('settings/', views.settings_view, name='settings'),
]
