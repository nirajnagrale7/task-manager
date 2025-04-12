from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'priority', 'due_date']
    search_fields = ['title', 'description']

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(
            assigned_by=user
        ) | Task.objects.filter(
            assigned_to=user
        )

    def perform_create(self, serializer):
        serializer.save(assigned_by=self.request.user)
