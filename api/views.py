from .models import Task
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class TaskListView(APIView):
    def get(self, request):
        tasks = Task.objects.all()

        priority = request.GET.get('priority')
        if priority:
            tasks = tasks.filter(priority=priority)

        completed = request.GET.get('completed')
        if completed:
            if completed.lower() == 'true':
                tasks = tasks.filter(completed=True)
            elif completed.lower() == 'false':
                tasks = tasks.filter(completed=False)

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TaskSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status=400)


class TaskDetailView(APIView):
    def get(self,request,id):
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExis:
            return Response({"error":"not found"},status=404)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    def put(self,request,id):
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response({"error":"not found"}, status=404)
        
        serializer = TaskSerializer(task,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        
        return Response(serializer.errors,status=400)
    
    def delete(self,request,id):
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response({"error":"not found"}, status=404)
        
        task.delete()
        return Response(status=204)
        
        





 




