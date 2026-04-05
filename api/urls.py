from .views import tasks
from django.urls import path
urlpatterns = [
    path('tasks/',tasks),
]