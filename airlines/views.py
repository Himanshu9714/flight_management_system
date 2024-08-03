from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .forms import AirlineForm
from .models import Airline


class AirlineListView(ListView):
    model = Airline
    template_name = "flights/airline_list.html"
    context_object_name = "airlines"
    paginate_by = 10  # Optional: Add pagination if the list of airlines is large

    def get_queryset(self):
        # Optional: Customize the queryset if needed
        return Airline.objects.all()


class AirlineCreateView(CreateView):
    model = Airline
    form_class = AirlineForm
    template_name = "flights/airline_form.html"
    success_url = reverse_lazy("airlines:airline_list")

    def form_valid(self, form):
        # Optional: Add any custom logic on form validation
        return super().form_valid(form)


class AirlineUpdateView(UpdateView):
    model = Airline
    form_class = AirlineForm
    template_name = "flights/airline_form.html"
    success_url = reverse_lazy("airlines:airline_list")

    def form_valid(self, form):
        # Optional: Add any custom logic on form validation
        return super().form_valid(form)


class AirlineDeleteView(DeleteView):
    model = Airline
    template_name = "flights/airline_confirm_delete.html"
    success_url = reverse_lazy("airlines:airline_list")

    def get(self, request, *args, **kwargs):
        # Handle GET request separately to ensure user confirmation
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        # Handle POST request for deletion
        return super().post(request, *args, **kwargs)
