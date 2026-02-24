"""Tests for shipping models."""
import pytest
from django.utils import timezone

from shipping.models import Carrier


@pytest.mark.django_db
class TestCarrier:
    """Carrier model tests."""

    def test_create(self, carrier):
        """Test Carrier creation."""
        assert carrier.pk is not None
        assert carrier.is_deleted is False

    def test_str(self, carrier):
        """Test string representation."""
        assert str(carrier) is not None
        assert len(str(carrier)) > 0

    def test_soft_delete(self, carrier):
        """Test soft delete."""
        pk = carrier.pk
        carrier.is_deleted = True
        carrier.deleted_at = timezone.now()
        carrier.save()
        assert not Carrier.objects.filter(pk=pk).exists()
        assert Carrier.all_objects.filter(pk=pk).exists()

    def test_queryset_excludes_deleted(self, hub_id, carrier):
        """Test default queryset excludes deleted."""
        carrier.is_deleted = True
        carrier.deleted_at = timezone.now()
        carrier.save()
        assert Carrier.objects.filter(hub_id=hub_id).count() == 0

    def test_toggle_active(self, carrier):
        """Test toggling is_active."""
        original = carrier.is_active
        carrier.is_active = not original
        carrier.save()
        carrier.refresh_from_db()
        assert carrier.is_active != original


