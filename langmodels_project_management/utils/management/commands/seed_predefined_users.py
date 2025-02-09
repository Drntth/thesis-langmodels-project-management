import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.auth.models import User
from users.models import UserProfile

class Command(BaseCommand):
    help = "Seed the database with predefined users and user profiles"

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()
        all_users = []

        user_password = "userPass123"
        staff_password = "staffPass123"
        superuser_password = "superuserPass123"

        predefined_users = [
            {"username": "user", "email": "user@example.com", "password": user_password, "is_staff": False, "is_superuser": False},
            {"username": "staff", "email": "staff@example.com", "password": staff_password, "is_staff": True, "is_superuser": False},
            {"username": "superuser", "email": "superuser@example.com", "password": superuser_password, "is_staff": True, "is_superuser": True},
        ]

        
        for user_data in predefined_users:
            user, created = User.objects.get_or_create(username=user_data["username"], defaults={
                "email": user_data["email"],
                "is_staff": user_data["is_staff"],
                "is_superuser": user_data["is_superuser"]
            })
            if created:
                user.set_password(user_data["password"]) 
                user.save()
            all_users.append(user)

        self.stdout.write(self.style.SUCCESS("Predefined users: user/userPass123, staff/staffPass123, superuser/superuserPass123"))