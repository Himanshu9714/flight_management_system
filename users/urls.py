from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import CustomLoginView
from .views import ProfileEditView

app_name = "users"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="users:login"), name="logout"),
    path("profile/edit/", ProfileEditView.as_view(), name="profile_edit"),
]
