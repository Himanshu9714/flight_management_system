from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import View

from .forms import BookingForm
from .models import Booking


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "flights/booking_list.html"
    context_object_name = "bookings"
    paginate_by = 10  # Number of bookings per page

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by("-booking_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_admin_user"] = self.request.user.role == "admin"
        return context


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "flights/booking_form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if not self.request.user.role == "admin":
            form.fields.pop("user")
        return form

    def form_valid(self, form):
        if not self.request.user.role == "admin":
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("bookings:booking_list")


class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = "flights/booking_detail.html"
    context_object_name = "booking"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not self.request.user.role == "admin" and obj.user != self.request.user:
            raise PermissionDenied
        return obj


class BookingCancelView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        booking = get_object_or_404(Booking, pk=kwargs["pk"])
        if request.user.role == "admin" or booking.user == request.user:
            booking.status = "canceled"
            booking.save()
        return redirect(reverse_lazy("bookings:booking_list"))
