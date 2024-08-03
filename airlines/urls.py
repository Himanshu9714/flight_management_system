from django.urls import path

from .views import *

app_name = "airlines"

urlpatterns = [
    path("", AirlineListView.as_view(), name="airline_list"),
    path("create", AirlineCreateView.as_view(), name="airline_create"),
    path("<int:pk>/edit", AirlineUpdateView.as_view(), name="airline_update"),
    path("<int:pk>/delete", AirlineDeleteView.as_view(), name="airline_delete"),
]
