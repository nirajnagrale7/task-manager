from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['assigned_by', 'created_at']

    def validate(self, data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            if data['assigned_to'] == request.user:
                raise serializers.ValidationError("You cannot assign a task to yourself.")
        return data