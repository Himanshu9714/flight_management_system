from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from .forms import CustomUserChangeFormUI
from .forms import ProfileForm
from .models import Profile


class CustomLoginView(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("dashboard:home")


class ProfileEditView(LoginRequiredMixin, View):
    template_name = "users/profile_edit.html"

    def get(self, request):
        user_form = CustomUserChangeFormUI(instance=request.user)
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(instance=profile)

        return render(
            request,
            self.template_name,
            {"user_form": user_form, "profile_form": profile_form},
        )

    def post(self, request):
        user_form = CustomUserChangeFormUI(request.POST, instance=request.user)
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse_lazy("dashboard:home"))

        return render(
            request,
            self.template_name,
            {"user_form": user_form, "profile_form": profile_form},
        )
