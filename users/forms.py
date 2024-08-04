from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name")
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }


class CustomUserChangeFormUI(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }


class CustomUserChangeFormUIwithEmail(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=False,  # Make password optional for updates
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=False,
        label="Confirm Password",
    )
    role = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-control"}),
        choices=[("admin", "Admin"), ("user", "User")],
        required=True,
    )

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "password"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        role = self.cleaned_data.get("role")

        if password:
            user.set_password(password)

        if commit:
            user.save()

        user.user_roles.create(role=role)
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_picture", "bio", "location", "birth_date"]
        widgets = {
            "profile_picture": forms.ClearableFileInput(
                attrs={"class": "form-control-file"}
            ),
            "bio": forms.Textarea(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "birth_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }
