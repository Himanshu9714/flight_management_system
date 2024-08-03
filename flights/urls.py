from django.urls import path

from .views import FlightCreateView
from .views import FlightDeleteView
from .views import FlightDetailView
from .views import FlightListView
from .views import FlightScheduleCreateView
from .views import FlightScheduleListView
from .views import FlightUpdateView

app_name = "flights"

urlpatterns = [
    path("", FlightListView.as_view(), name="flight_list"),
    path("create/", FlightCreateView.as_view(), name="flight_create"),
    path("<int:pk>/edit/", FlightUpdateView.as_view(), name="flight_update"),
    path("<int:pk>/delete/", FlightDeleteView.as_view(), name="flight_delete"),
    path("<int:pk>/detail/", FlightDetailView.as_view(), name="flight_detail"),
    path("schedule/", FlightScheduleListView.as_view(), name="flight_schedule_list"),
    path(
        "schedule/create/",
        FlightScheduleCreateView.as_view(),
        name="flight_schedule_create",
    ),
]
