from django.urls import path
from . import views

app_name = 'tests'
urlpatterns = [
	# test
	path('test/', views.test, name='test'),
]