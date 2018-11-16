from django import forms


class LocationForm(forms.Form):
    """LocationForm definition."""

    location = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
