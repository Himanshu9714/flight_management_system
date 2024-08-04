from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .models import CustomUser
from .models import Profile
from .models import UserRole


@receiver(post_migrate)
def create_super_admin(sender, **kwargs):
    # Create the superuser
    if not CustomUser.objects.filter(email="sa@gmail.com").exists():
        user = CustomUser.objects.create_superuser(
            email="sa@gmail.com",
            first_name="Super",
            last_name="Admin",
            password="Admin@123",
        )
        UserRole.objects.create(user=user, role="admin")
        Profile.objects.create(user=user, location="India")

    # Create the normal user
    if not CustomUser.objects.filter(email="ram@gmail.com").exists():
        user = CustomUser.objects.create_user(
            email="ram@gmail.com",
            first_name="Shree",
            last_name="Ram",
            password="Hanuman@123",
        )
        UserRole.objects.create(user=user, role="user")
        Profile.objects.create(user=user, location="India")
