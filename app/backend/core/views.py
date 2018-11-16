from backend.core.forms import LocationForm

from django.views.generic.edit import FormView


class TemperatureByLocationFormView(FormView):
    """FormView to get temperature according to inserted location"""
    form_class = LocationForm
    template_name = 'core/location_form.html'
