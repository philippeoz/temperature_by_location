from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from backend.core.forms import LocationForm
from backend.core.models import IPRequestLog


class TemperatureByLocationFormView(FormView):
    """FormView to get temperature according to inserted location"""
    form_class = LocationForm
    template_name = 'core/location_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.request.session['search_data'] = form.result
        ip = self.request.META.get('HTTP_X_FORWARDED_FOR', None)
        IPRequestLog.objects.create(
            ip=ip or self.request.META.get('REMOTE_ADDR')
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        self.request.session['search_data'] = None
        return super().form_invalid(form)
