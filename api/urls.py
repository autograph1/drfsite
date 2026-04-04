from .views import get_tasks
from django.urls import path
urlpatterns = [
    path('tasks/',get_tasks),
]