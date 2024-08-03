from django.urls import path

from .views import *

app_name = "airports"

urlpatterns = [
    path("", AirportListView.as_view(), name="airport_list"),
    path("create", AirportCreateView.as_view(), name="airport_create"),
    path("<int:pk>/edit", AirportUpdateView.as_view(), name="airport_update"),
    path("<int:pk>/delete", AirportDeleteView.as_view(), name="airport_delete"),
]
