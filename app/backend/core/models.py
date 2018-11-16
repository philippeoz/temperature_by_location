from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class IPRequestLog(models.Model):
    """Model definition for IPRequestLog."""

    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for IPRequestLog."""

        verbose_name = _('IPRequestLog')
        verbose_name_plural = _('IPRequestLogs')

    def __str__(self):
        """Unicode representation of IPRequestLog."""
        return self.ip


class TemperatureRequestCache(models.Model):
    """Model definition for TemperatureRequestCache."""

    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for TemperatureRequestCache."""

        verbose_name = _('TemperatureRequestCache')
        verbose_name_plural = _('TemperatureRequestCaches')

    def __str__(self):
        """Unicode representation of TemperatureRequestCache."""
        return f'{self.latitude}, {self.longitude} - {temperature}° C'
    
    @classmethod
    def clear_created_more_than_an_hour_ago(cls):
        """ Delete all logs created more than an hour ago """
        one_hour_ago = timezone.now() - timezone.timedelta(seconds=3600)
        queryset = cls.objects.filter(created_at__lt=one_hour_ago)
        queryset.delete()
