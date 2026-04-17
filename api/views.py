from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Task
from .serializers import TaskSerializer

class TaskListView(ListCreateAPIView):
    serializer_class = TaskSerializer
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
        
        





 




