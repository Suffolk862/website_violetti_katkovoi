from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Task
from .forms import TaskForm

def index(request):
	"""Home page app viokat_apps"""
	return render(request, 'viokat_apps/index.html')

def teacher(request):
	"""Teacher"""
	return render(request, 'viokat_apps/teacher.html')	

def task(request):
	"""Task"""
	tasks = Task.objects.order_by('date_added')
	context = {'tasks': tasks}
	return render(request, 'viokat_apps/task.html', context)

def new_task(request):
	"""Определяет новое задание"""
	if request.method != 'POST':
		#Данные не отправлялись; создается пустая форма.
		form = TaskForm()
	else:
		#Отправлены данные POST; обработать данные.
		form = TaskForm(data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('viokat_apps:task'))

	context = {'form': form}
	return render(request, 'viokat_apps/new_task.html', context)

def registration(request):
	"""Registration"""
	return render(request, '')


