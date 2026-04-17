from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Task
from .serializers import TaskSerializer

class TaskListView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
        
        





 




