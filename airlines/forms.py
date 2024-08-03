from django import forms

from .models import Airline


class AirlineForm(forms.ModelForm):
    class Meta:
        model = Airline
        fields = ["name", "logo"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter airline name"}
            ),
            "logo": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {"class": "form-control"}
            )  # Apply Bootstrap styling to all form fields
