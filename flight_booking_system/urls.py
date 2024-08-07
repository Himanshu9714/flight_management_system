"""
URL configuration for flight_booking_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include
from django.urls import path


def redirect_to_login(request):
    if request.user.is_authenticated:
        return redirect("dashboard:home")  # Adjust this to the name of your home view
    else:
        return redirect("users:login")  # Adjust this to the name of your login view


urlpatterns = [
    path("", redirect_to_login, name="redirect_to_login"),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("flights/", include("flights.urls")),
    path("airlines/", include("airlines.urls")),
    path("airports/", include("airports.urls")),
    path("bookings/", include("bookings.urls")),
]


# TODO: the static endpoint handling should be removed from here in production environment
# and needs to use nginx or apache configurations for the same.
# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
