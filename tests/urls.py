from django.urls import path
from . import views

app_name = 'tests'
urlpatterns = [
	path('test/', views.test, name='test'),
]
