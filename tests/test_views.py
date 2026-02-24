"""Tests for shipping views."""
import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestDashboard:
    """Dashboard view tests."""

    def test_dashboard_loads(self, auth_client):
        """Test dashboard page loads."""
        url = reverse('shipping:dashboard')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_dashboard_htmx(self, auth_client):
        """Test dashboard HTMX partial."""
        url = reverse('shipping:dashboard')
        response = auth_client.get(url, HTTP_HX_REQUEST='true')
        assert response.status_code == 200

    def test_dashboard_requires_auth(self, client):
        """Test dashboard requires authentication."""
        url = reverse('shipping:dashboard')
        response = client.get(url)
        assert response.status_code == 302


@pytest.mark.django_db
class TestCarrierViews:
    """Carrier view tests."""

    def test_list_loads(self, auth_client):
        """Test list view loads."""
        url = reverse('shipping:carriers_list')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_list_htmx(self, auth_client):
        """Test list HTMX partial."""
        url = reverse('shipping:carriers_list')
        response = auth_client.get(url, HTTP_HX_REQUEST='true')
        assert response.status_code == 200

    def test_list_search(self, auth_client):
        """Test list search."""
        url = reverse('shipping:carriers_list')
        response = auth_client.get(url, {'q': 'test'})
        assert response.status_code == 200

    def test_list_sort(self, auth_client):
        """Test list sorting."""
        url = reverse('shipping:carriers_list')
        response = auth_client.get(url, {'sort': 'created_at', 'dir': 'desc'})
        assert response.status_code == 200

    def test_export_csv(self, auth_client):
        """Test CSV export."""
        url = reverse('shipping:carriers_list')
        response = auth_client.get(url, {'export': 'csv'})
        assert response.status_code == 200
        assert 'text/csv' in response['Content-Type']

    def test_export_excel(self, auth_client):
        """Test Excel export."""
        url = reverse('shipping:carriers_list')
        response = auth_client.get(url, {'export': 'excel'})
        assert response.status_code == 200

    def test_add_form_loads(self, auth_client):
        """Test add form loads."""
        url = reverse('shipping:carrier_add')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_add_post(self, auth_client):
        """Test creating via POST."""
        url = reverse('shipping:carrier_add')
        data = {
            'name': 'New Name',
            'code': 'New Code',
            'tracking_url': 'https://example.com',
            'is_active': 'on',
        }
        response = auth_client.post(url, data)
        assert response.status_code == 200

    def test_edit_form_loads(self, auth_client, carrier):
        """Test edit form loads."""
        url = reverse('shipping:carrier_edit', args=[carrier.pk])
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_edit_post(self, auth_client, carrier):
        """Test editing via POST."""
        url = reverse('shipping:carrier_edit', args=[carrier.pk])
        data = {
            'name': 'Updated Name',
            'code': 'Updated Code',
            'tracking_url': 'https://example.com',
            'is_active': '',
        }
        response = auth_client.post(url, data)
        assert response.status_code == 200

    def test_delete(self, auth_client, carrier):
        """Test soft delete via POST."""
        url = reverse('shipping:carrier_delete', args=[carrier.pk])
        response = auth_client.post(url)
        assert response.status_code == 200
        carrier.refresh_from_db()
        assert carrier.is_deleted is True

    def test_toggle_status(self, auth_client, carrier):
        """Test toggle active status."""
        url = reverse('shipping:carrier_toggle_status', args=[carrier.pk])
        original = carrier.is_active
        response = auth_client.post(url)
        assert response.status_code == 200
        carrier.refresh_from_db()
        assert carrier.is_active != original

    def test_bulk_delete(self, auth_client, carrier):
        """Test bulk delete."""
        url = reverse('shipping:carriers_bulk_action')
        response = auth_client.post(url, {'ids': str(carrier.pk), 'action': 'delete'})
        assert response.status_code == 200
        carrier.refresh_from_db()
        assert carrier.is_deleted is True

    def test_list_requires_auth(self, client):
        """Test list requires authentication."""
        url = reverse('shipping:carriers_list')
        response = client.get(url)
        assert response.status_code == 302


@pytest.mark.django_db
class TestSettings:
    """Settings view tests."""

    def test_settings_loads(self, auth_client):
        """Test settings page loads."""
        url = reverse('shipping:settings')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_settings_requires_auth(self, client):
        """Test settings requires authentication."""
        url = reverse('shipping:settings')
        response = client.get(url)
        assert response.status_code == 302

