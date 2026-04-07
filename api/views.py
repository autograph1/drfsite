from django.shortcuts import render
from .models import Task
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

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
def tasks(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        data = decode(tasks)
        return JsonResponse(data,safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        Task.objects.create(
            title = data["title"],
            priority = data["priority"]
        )
        return JsonResponse({"status":"ok"})
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)
    
@csrf_exempt
def task_detail(request,id):

    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:   
        return JsonResponse({"error" : "Not found"}, status = 404)
    if request.method == "GET":
        data = {
        "id" : task.id, 
        'title' : task.title,
        "created_at" : task.created_at,
        "priority" : task.priority,
        "completed" : task.completed,
        }
        return JsonResponse(data)
    elif request.method == "DELETE":
        task.delete()
        return JsonResponse({"status" : "deleted"})
    else:
        return JsonResponse({"error" : "Invalid method"}, status = 405)
 




