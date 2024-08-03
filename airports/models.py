from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Airport(models.Model):
    code = models.CharField(
        max_length=10, unique=True, help_text="Airport code, e.g., JFK, LAX"
    )
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("airport")
        verbose_name_plural = _("airports")

    def __str__(self):
        return f"{self.name} ({self.code})"
