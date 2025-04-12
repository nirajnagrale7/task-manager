# generate_tasks.py

import os
import django
import random
from datetime import timedelta
from django.utils import timezone

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_manager.settings")  # change if your settings module name is different
django.setup()

from tasks.models import Task
from django.contrib.auth.models import User

# Fetch users
assigned_by = User.objects.filter(is_superuser=True).first()
assigned_users = User.objects.exclude(id=assigned_by.id)

titles = [
    "Complete Report", "Fix Bug", "Team Meeting", "Code Review", "Write Tests",
    "Design Homepage", "Optimize Query", "Update Docs", "Deploy to Prod", "Security Audit"
]

# Create 30 dummy tasks
for i in range(30):
    Task.objects.create(
        title=random.choice(titles) + f" #{i}",
        description="Auto-generated task for pagination testing.",
        status=random.choice([1, 2, 3]),
        priority=random.choice([1, 2]),
        due_date=timezone.now().date() + timedelta(days=random.randint(1, 30)),
        assigned_to=random.choice(assigned_users),
        assigned_by=assigned_by,
    )

print("✅ 30 Temp tasks created successfully.")
