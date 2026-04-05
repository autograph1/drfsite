from .views import get_tasks, post_task
from django.urls import path
urlpatterns = [
    path('tasks/',get_tasks),
    path('post_task/',post_task),
]