"""
Shipping & Delivery Module Views
"""
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.modules_runtime.navigation import with_module_nav


@login_required
@with_module_nav('shipping', 'dashboard')
@htmx_view('shipping/pages/dashboard.html', 'shipping/partials/dashboard_content.html')
def dashboard(request):
    """Dashboard view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('shipping', 'shipments')
@htmx_view('shipping/pages/shipments.html', 'shipping/partials/shipments_content.html')
def shipments(request):
    """Shipments view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('shipping', 'carriers')
@htmx_view('shipping/pages/carriers.html', 'shipping/partials/carriers_content.html')
def carriers(request):
    """Carriers view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('shipping', 'settings')
@htmx_view('shipping/pages/settings.html', 'shipping/partials/settings_content.html')
def settings(request):
    """Settings view."""
    hub_id = request.session.get('hub_id')
    return {}

