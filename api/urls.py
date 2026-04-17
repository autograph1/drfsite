from .views import TaskDetailView, TaskListView
from django.urls import path
urlpatterns = [
    path('tasks/',TaskListView.as_view()),
    path('tasks/<int:pk>/',TaskDetailView.as_view())
]