from django.shortcuts import render
from .models import Task
from django.http import JsonResponse



def get_tasks(request):
    tasks = Task.objects.all()
    data = decode(tasks)
    return JsonResponse(data,safe=False)


def decode(tasks):
    result = []

    for task in tasks:
        result.append({
        "title": task.title,
        "created_at": task.created_at,
        "completed": task.completed,
        "priority": task.priority
    })
    return result

