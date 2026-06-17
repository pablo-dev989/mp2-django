from django import forms

from phoneapp.models import Manufacturer, Smartphone


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name', 'origin', 'foundation', 'website']
        widgets = {
            'foundation': forms.DateInput(attrs={'type': 'date'}),
        }

class SmartphoneForm(forms.ModelForm):
    screen_size = forms.DecimalField(required=True, label="Tamaño de pantalla (pulgadas)")

    class Meta:
        model = Smartphone
        fields = ['manufacturer', 'name', 'ram', 'memory_capacity', 'screen_size']