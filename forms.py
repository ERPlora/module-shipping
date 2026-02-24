from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Carrier

class CarrierForm(forms.ModelForm):
    class Meta:
        model = Carrier
        fields = ['name', 'code', 'tracking_url', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'code': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'tracking_url': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'url'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'toggle'}),
        }

