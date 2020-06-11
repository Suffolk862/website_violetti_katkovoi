from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm

def index(request):
	"""Home page app main"""
	return render(request, 'main/index.html')

def teacher(request):
	"""Teacher"""
	return render(request, 'main/teacher.html')	

@login_required
def task(request):
	"""Task"""
	tasks = Task.objects.order_by('date_added')
	context = {'tasks': tasks}
	return render(request, 'main/task.html', context)

@login_required
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
			return HttpResponseRedirect(reverse('main:task'))

	context = {'form': form}
	return render(request, 'main/new_task.html', context)

def registration(request):
	"""Registration"""
	return render(request, '')


