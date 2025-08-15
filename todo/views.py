from django.shortcuts import render, redirect
from .models import Task

# This view will handle displaying all tasks
def taskList(request):
    tasks = Task.objects.all().order_by('-created_at') # Get all tasks, newest first
    context = {'tasks': tasks}
    return render(request, 'todo/main.html', context)

# This view will handle the creation of a new task
def taskCreate(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title: # Ensure the title is not empty
            Task.objects.create(title=title)
    return redirect('task-list')

# This view will handle editing a task's title
def taskEdit(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        new_title = request.POST.get('title')
        if new_title:
            task.title = new_title
            task.save()
    return redirect('task-list')

# This view will handle updating a task (marking it as complete/incomplete)
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = not task.completed # Toggle the completed status
    task.save()
    return redirect('task-list')

# This view will handle deleting a task
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('task-list')
