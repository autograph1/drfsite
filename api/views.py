from django.shortcuts import render
from .models import Task

tasks = Task.objects.all()

result = []
for task in tasks:
    result.append({
    "title": task.title,
    "created_at": task.created_at,
    "completed": task.completed,
    "priority": task.priority
})

