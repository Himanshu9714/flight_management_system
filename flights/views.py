from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from flight_booking_system.mixins import AdminRequiredMixin

from .forms import FlightForm
from .forms import FlightScheduleForm
from .models import Flight
from .models import FlightSchedule


class FlightListView(ListView):
    model = Flight
    template_name = "flights/flight_list.html"
    context_object_name = "flights"
    paginate_by = 10  # Number of flights per page

    def get_queryset(self):
        return Flight.objects.all().order_by("departure_time")


class FlightCreateView(CreateView, AdminRequiredMixin):
    model = Flight
    form_class = FlightForm
    template_name = "flights/flight_form.html"
    success_url = reverse_lazy("flights:flight_list")


class FlightUpdateView(UpdateView, AdminRequiredMixin):
    model = Flight
    form_class = FlightForm
    template_name = "flights/flight_form.html"
    success_url = reverse_lazy("flights:flight_list")


class FlightDeleteView(DeleteView, AdminRequiredMixin):
    model = Flight
    template_name = "flights/flight_confirm_delete.html"
    success_url = reverse_lazy("flights:flight_list")


class FlightDetailView(DetailView):
    model = Flight
    template_name = "flights/flight_detail.html"
    context_object_name = "flight"


class FlightScheduleListView(ListView):
    model = FlightSchedule
    template_name = "flights/flight_schedule_list.html"
    context_object_name = "schedules"
    paginate_by = 10  # Number of schedules per page

    def get_queryset(self):
        return FlightSchedule.objects.all().order_by("schedule_date", "departure_time")


class FlightScheduleCreateView(CreateView, AdminRequiredMixin):
    model = FlightSchedule
    form_class = FlightScheduleForm
    template_name = "flights/flight_schedule_form.html"
    success_url = reverse_lazy("flights:flight_schedule_list")
