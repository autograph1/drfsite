from .views import tasks, tasks_detail
from django.urls import path
urlpatterns = [
    path('tasks/',tasks),
    path('tasks/<int:id>/',tasks_detail)
]