from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from airlines.models import Airline
from airports.models import Airport


class Flight(models.Model):
    flight_number = models.CharField(max_length=20, unique=True)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    departure_airport = models.ForeignKey(
        Airport, related_name="departures", on_delete=models.CASCADE
    )
    arrival_airport = models.ForeignKey(
        Airport, related_name="arrivals", on_delete=models.CASCADE
    )
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    duration = models.DurationField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seats_available = models.PositiveIntegerField(default=60)

    class Meta:
        verbose_name = _("flight")
        verbose_name_plural = _("flights")
        ordering = ["departure_time"]

    def __str__(self):
        return f"{self.flight_number} ({self.airline})"


class FlightSchedule(models.Model):
    flight = models.ForeignKey(
        Flight, on_delete=models.CASCADE, related_name="flight_schedule"
    )
    schedule_date = models.DateField()
    departure_time = models.TimeField()
    arrival_time = models.TimeField()

    class Meta:
        verbose_name = _("flight schedule")
        verbose_name_plural = _("flight schedules")

    def __str__(self):
        return f"{self.flight.flight_number} on {self.schedule_date}"
