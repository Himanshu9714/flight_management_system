from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Airline(models.Model):
    name = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to="airline_logos/", blank=True, null=True)

    class Meta:
        verbose_name = _("airline")
        verbose_name_plural = _("airlines")

    def __str__(self):
        return self.name
