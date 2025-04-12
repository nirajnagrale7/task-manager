# tasks/models.py

from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = (
        (1, 'Open'),
        (2, 'In Progress'),
        (3, 'Done'),
        (4, 'Overdue'),
    )

    PRIORITY_CHOICES = (
        (1, 'Low'),
        (2, 'High'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_by = models.ForeignKey(User, related_name='assigned_by', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='assigned_to', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
