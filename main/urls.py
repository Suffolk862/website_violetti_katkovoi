from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
	# home page
	path('', views.index, name='index'),

	# teacher
	path('teacher/', views.teacher, name='teacher'),

	# task
	path('task/', views.task, name='task'),

	# new task
	path('new_task/', views.new_task, name='new_task'),
]
