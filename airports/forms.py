from django import forms

from .models import Airport


class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ["code", "name", "city", "country"]
        widgets = {
            "code": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter airport code"}
            ),
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter airport name"}
            ),
            "city": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter city"}
            ),
            "country": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter country"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {"class": "form-control"}
            )  # Apply Bootstrap styling to all form fields
