from .views import tasks, task_detail
from django.urls import path
urlpatterns = [
    path('tasks/',tasks),
    path('tasks/<int:id>/',task_detail)
]