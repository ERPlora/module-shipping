from django.urls import path
from . import views

app_name = 'shipping'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('shipments/', views.shipments, name='shipments'),
    path('carriers/', views.carriers, name='carriers'),
    path('settings/', views.settings, name='settings'),
]
