from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from .forms import TaskForm

@login_required
def dashboard(request):
	tasks = Task.objects.filter(user=request.user).order_by('-created_at')
	return render(request, 'tasks/dashboard.html', {'tasks': tasks})

@login_required
def add_task(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			task = form.save(commit=False)
			task.user = request.user
			task.save()
			messages.success(request, 'Task added successfully!')
			return redirect('dashboard')
	else:
		form = TaskForm()
	return render(request, 'tasks/add_task.html', {'form': form})

@login_required
def edit_task(request, task_id):
	task = get_object_or_404(Task, id=task_id, user=request.user)
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			messages.success(request, 'Task updated successfully!')
			return redirect('dashboard')
	else:
		form = TaskForm(instance=task)
	return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

@login_required
def delete_task(request, task_id):
	task = get_object_or_404(Task, id=task_id, user=request.user)
	if request.method == 'POST':
		task.delete()
		messages.success(request, 'Task deleted successfully!')
		return redirect('dashboard')
	return render(request, 'tasks/delete_task.html', {'task': task})

@login_required
def toggle_task(request, task_id):
	task = get_object_or_404(Task, id=task_id, user=request.user)
	if task.status == 'completed':
		task.status = 'pending'
	else:
		task.status = 'completed'
	task.save()
	return redirect('dashboard')
