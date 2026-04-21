from django.urls import path
from . import views

app_name = 'taskhero'

urlpatterns = [
    path('', views.home, name='home'),
    path('task-detail/<int:task_pk>/', views.task_detail, name='task_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-task/', views.create_task, name='create_task'),
]