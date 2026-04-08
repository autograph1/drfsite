from rest_framework import serializers
from .models import PRIORITY_CHOICES

class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    completed = serializers.BooleanField()
    priority = serializers.ChoiceField(choices=PRIORITY_CHOICES)
    created_at = serializers.DateTimeField(read_only=True)