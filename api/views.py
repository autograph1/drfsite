from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Task
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from .permissions import IsOwner

class TaskListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = TaskSerializer
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
        
        





 




