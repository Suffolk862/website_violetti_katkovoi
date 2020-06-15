from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm


def index(request):
	"""Home page main app"""
	return render(request, 'main/index.html')


def teacher(request):
	return render(request, 'main/teacher.html')


@login_required
def task(request):
	tasks = Task.objects.order_by('date_added')
	context = {'tasks': tasks}
	return render(request, 'main/task.html', context)


@login_required
def new_task(request):
	if request.method != 'POST':
		form = TaskForm()
	else:
		form = TaskForm(data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('main:task'))

	context = {'form': form}
	return render(request, 'main/new_task.html', context)


def registration(request):
	return render(request, '')
