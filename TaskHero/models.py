from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()
class Task(models.Model):
    class Status(models.TextChoices):
        TO_DO = 'td', 'To Do'
        IN_PROGRESS = 'ip', 'In Progress'
        COMPLETED = 'cmp', 'Completed'
    class Priority(models.TextChoices):
        LOW = 'low', 'Low'
        MEDIUM = 'mid', 'Medium'
        HIGH = 'high', 'High'
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=3, choices=Status, default=Status.TO_DO)
    priority = models.CharField(max_length=4, choices=Priority, default=Priority.MEDIUM)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
