from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Task
from .forms import TaskForm
# Create your views here.

def home(request):
    return render(request, 'taskhero/index.html')

@login_required
def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.added_by = request.user
            task.save()
            return redirect('taskhero:task_detail', request.user)
        
    return render(request, 'taskhero/create-task.html', {'form': form})

@login_required
def task_detail(request, task_pk):
    task = get_object_or_404(Task, pk = task_pk, user=request.user)
    return render(request, 'taskhero/task-detail.html', {'task': task})


@login_required
def dashboard(request):
    tasks = Task.objects.filter(added_by=request.user)
    return render(request, 'taskhero/dashboard.html', {'tasks': tasks})