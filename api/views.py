from .models import Task
from django.views.decorators.csrf import csrf_exempt
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

@csrf_exempt
class TaskListView(APIView):
    def get(self,request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks,many=True) 
        return Response(serializer.data,status=200)
    
    def post(self,request):
        serializer = TaskSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status=400)



@csrf_exempt

class TaskDetailView(APIView):

 




