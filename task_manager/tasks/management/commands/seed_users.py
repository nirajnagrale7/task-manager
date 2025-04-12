from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Seed initial users"

    def handle(self, *args, **kwargs):
        users = [
            {"username": "admin_user", "email": "admin@example.com", "password": "admin123"},
            {"username": "john_doe", "email": "john@example.com", "password": "john123"},
            {"username": "jane_smith", "email": "jane@example.com", "password": "jane123"},
        ]

        for user_data in users:
            if not User.objects.filter(username=user_data["username"]).exists():
                user = User.objects.create_user(
                    username=user_data["username"],
                    email=user_data["email"],
                    password=user_data["password"]
                )
                self.stdout.write(self.style.SUCCESS(f"Created user: {user.username}"))
            else:
                self.stdout.write(f"User {user_data['username']} already exists.")
