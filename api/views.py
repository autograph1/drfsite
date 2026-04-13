from django.shortcuts import render
from .models import Task
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

@csrf_exempt
def tasks(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)
        
    elif request.method == "POST":
        data = json.loads(request.body)
        serializer = TaskSerializer(data=data) 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        else:
            return JsonResponse(serializer.errors, status = 400)


    
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
    elif request.method == "PUT":
        data = json.loads(request.body)
        task.title = data.get("title", task.title)
        task.priority = data.get("priority", task.priority)
        task.completed = data.get("completed", task.completed)
        task.save()
        return JsonResponse({"status": "updated"}) 
    else:
        return JsonResponse({"error" : "Invalid method"}, status = 405)
    
@csrf_exempt
class TaskListView(APIView):
    def get(self,request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks,many=True) 
        return Response(serializer.data,status=200)
    

    def post(self,request):
        task = TaskSerializer(request.data) 
        return
 




