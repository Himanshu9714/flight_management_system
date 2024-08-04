from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from flights.models import Flight


class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings"
    )
    flight = models.ForeignKey(
        Flight, on_delete=models.CASCADE, related_name="bookings"
    )
    booking_date = models.DateTimeField(auto_now_add=True)
    seat_number = models.CharField(max_length=10, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=10,
        choices=[("confirmed", _("Confirmed")), ("canceled", _("Canceled"))],
        default="confirmed",
    )

    class Meta:
        verbose_name = _("booking")
        verbose_name_plural = _("bookings")

    def __str__(self):
        return f"Booking {self.id} - {self.flight.flight_number} by {self.user.email}"

    def clean(self):
        super().clean()
        if self.status == "confirmed":
            # Check if the seat is already booked
            if Booking.objects.filter(
                flight=self.flight, seat_number=self.seat_number, status="confirmed"
            ).exists():
                raise ValidationError(_("This seat is already booked."))

            # Check if the seat number exceeds available seats
            if int(self.seat_number) > self.flight.seats_available:
                raise ValidationError(
                    _("The seat number exceeds the available seats of the flight.")
                )


class Seat(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="seats")
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("seat")
        verbose_name_plural = _("seats")
        unique_together = ("flight", "seat_number")

    def __str__(self):
        return f"{self.seat_number} on flight {self.flight.flight_number}"
