from django.urls import path

from .views import *

app_name = "bookings"

urlpatterns = [
    path("", BookingListView.as_view(), name="booking_list"),
    path("create", BookingCreateView.as_view(), name="booking_create"),
    path("<int:pk>/cancel", BookingCancelView.as_view(), name="booking_cancel"),
    path("<int:pk>/detail", BookingDetailView.as_view(), name="booking_detail"),
]
