from django import forms

from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["flight", "seat_number", "price"]
        widgets = {
            "flight": forms.Select(attrs={"class": "form-control"}),
            "seat_number": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }
