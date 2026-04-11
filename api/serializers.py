from rest_framework import serializers
from .models import PRIORITY_CHOICES, Task

class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    completed = serializers.BooleanField()
    priority = serializers.ChoiceField(choices=PRIORITY_CHOICES)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)
