"""Patterns URL for viokat_apps"""

from django.urls import path
from . import views

app_name = 'viokat_apps'
urlpatterns = [
	# home page
	path('', views.index, name='index'),

	# teacher
	path('teacher/', views.teacher, name='teacher'),

	# task
	path('task/', views.task, name='task'),

	# new task
	path('new_task', views.new_task, name='new_task'),

	#registration
	path('registration/', views.registration, name='registration')
]