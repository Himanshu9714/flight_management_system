from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import CustomLoginView
from .views import ProfileEditView
from .views import UserCreateView
from .views import UserDeleteView
from .views import UserListView

app_name = "users"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="users:login"), name="logout"),
    path("profile/edit/", ProfileEditView.as_view(), name="profile_edit"),
    path("admin/users/", UserListView.as_view(), name="user_list"),
    path("admin/users/create/", UserCreateView.as_view(), name="user_create"),
    path("admin/users/<int:pk>/edit/", ProfileEditView.as_view(), name="user_update"),
    path("admin/users/<int:pk>/delete/", UserDeleteView.as_view(), name="user_delete"),
]
