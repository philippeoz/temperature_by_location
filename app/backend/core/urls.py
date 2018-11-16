from django.urls import path

from backend.core import views as core_views


urlpatterns = [
    path('', core_views.TemperatureByLocationFormView.as_view(), name='home'),
]
