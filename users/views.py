from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView

from flight_booking_system.mixins import AdminRequiredMixin

from .forms import CustomUserChangeFormUI
from .forms import CustomUserChangeFormUIwithEmail
from .forms import ProfileForm
from .models import CustomUser
from .models import Profile


class CustomLoginView(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("dashboard:home")


class ProfileEditView(LoginRequiredMixin, View):
    template_name = "users/profile_edit.html"

    def get(self, request, **kwargs):
        user_id = kwargs.get("pk")
        if (
            request.user.role == "admin"
            and user_id is not None
            and int(user_id) != int(request.user.id)
        ):
            user = CustomUser.objects.get(id=user_id)
        else:
            user = request.user
        user_form = CustomUserChangeFormUI(instance=user)
        profile, created = Profile.objects.get_or_create(user=user)
        profile_form = ProfileForm(instance=profile)

        return render(
            request,
            self.template_name,
            {"user_form": user_form, "profile_form": profile_form},
        )

    def post(self, request, **kwargs):
        user_id = kwargs.get("pk")
        is_admin_user = request.user.role == "admin"
        if (
            is_admin_user
            and user_id is not None
            and int(user_id) != int(request.user.id)
        ):
            user = CustomUser.objects.get(id=user_id)
        else:
            user = request.user

        user_form = CustomUserChangeFormUI(request.POST, instance=user)
        profile, created = Profile.objects.get_or_create(user=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            if is_admin_user:
                return redirect(reverse_lazy("users:user_list"))
            return redirect(reverse_lazy("dashboard:home"))

        return render(
            request,
            self.template_name,
            {"user_form": user_form, "profile_form": profile_form},
        )


class UserListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = CustomUser
    template_name = "users/user_list.html"
    context_object_name = "users"
    paginate_by = 10  # Number of users per page

    def get_queryset(self):
        query = self.request.GET.get("search", "")
        queryset = CustomUser.objects.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(email__icontains=query)
        ).exclude(id=self.request.user.id)
        return queryset


class UserCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = CustomUser
    form_class = CustomUserChangeFormUIwithEmail
    template_name = "users/user_form.html"
    success_url = reverse_lazy("users:user_list")

    def post(self, request):
        user_form = CustomUserChangeFormUIwithEmail(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form.instance.user_id = user.id
            profile_form.save()
            return redirect(reverse_lazy("users:user_list"))

        return render(
            request,
            self.template_name,
            {"user_form": user_form, "profile_form": profile_form},
        )


class UserDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = CustomUser
    template_name = "users/user_confirm_delete.html"
    success_url = reverse_lazy("users:user_list")
