from django.shortcuts import render
from .models import Task
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt



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
@csrf_exempt
def post_task(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Task.objects.create(
            title = data["title"],
            priority = data["priority"]
        )
        return JsonResponse({"status":"ok"})
        
    else:
        return(JsonResponse({"error": "Invalid method"}))


