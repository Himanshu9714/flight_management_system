from django import forms

from .models import Flight
from .models import FlightSchedule


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = [
            "flight_number",
            "airline",
            "departure_airport",
            "arrival_airport",
            "departure_time",
            "arrival_time",
            "duration",
            "price",
            "seats_available",
        ]
        widgets = {
            "flight_number": forms.TextInput(attrs={"class": "form-control"}),
            "airline": forms.Select(attrs={"class": "form-control"}),
            "departure_airport": forms.Select(attrs={"class": "form-control"}),
            "arrival_airport": forms.Select(attrs={"class": "form-control"}),
            "departure_time": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "arrival_time": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "duration": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "seats_available": forms.NumberInput(attrs={"class": "form-control"}),
        }


class FlightScheduleForm(forms.ModelForm):
    class Meta:
        model = FlightSchedule
        fields = ["flight", "schedule_date", "departure_time", "arrival_time"]
        widgets = {
            "flight": forms.Select(attrs={"class": "form-control"}),
            "schedule_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "departure_time": forms.TimeInput(
                attrs={"class": "form-control", "type": "time"}
            ),
            "arrival_time": forms.TimeInput(
                attrs={"class": "form-control", "type": "time"}
            ),
        }
