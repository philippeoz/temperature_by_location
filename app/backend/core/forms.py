from django import forms

from backend.core.utils import APIClient


class LocationForm(forms.Form):
    """LocationForm definition."""

    location = forms.CharField(required=True)

    def clean_location(self):
        data = self.cleaned_data['location']
        try:
            self.result = APIClient.get_or_create_temperature_info(data)
        except Exception as inst:
            raise forms.ValidationError(f'{inst}')
        return data
