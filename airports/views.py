from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .forms import AirportForm
from .models import Airport


class AirportListView(ListView):
    model = Airport
    template_name = "flights/airport_list.html"
    context_object_name = "airports"
    paginate_by = 10  # Number of airports per page

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("search", "")
        if search_query:
            queryset = queryset.filter(
                Q(code__icontains=search_query)
                | Q(name__icontains=search_query)
                | Q(city__icontains=search_query)
                | Q(country__icontains=search_query)
            )
        return queryset


class AirportCreateView(CreateView):
    model = Airport
    form_class = AirportForm
    template_name = "flights/airport_form.html"
    success_url = reverse_lazy("airports:airport_list")


class AirportUpdateView(UpdateView):
    model = Airport
    form_class = AirportForm
    template_name = "flights/airport_form.html"
    success_url = reverse_lazy("airports:airport_list")


class AirportDeleteView(DeleteView):
    model = Airport
    template_name = "flights/airport_confirm_delete.html"
    success_url = reverse_lazy("airports:airport_list")
