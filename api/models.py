from django.db import models


PRIORITY_CHOICES = [('low', 'Low'), ('medium', 'Medium'), ('high','High')]
class Task(models.Model):
    title = models.CharField(max_length = 255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length = 6, choices = PRIORITY_CHOICES)
