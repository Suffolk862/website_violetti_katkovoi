"""Patterns URL for users"""

from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'
urlpatterns = [    
	# Страница входа 	   
	path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),

	# Для выхода 
	path('logout/', views.logout_view, name='logout'),
	
	# Страница регистрации
	path('registration/', views.registration, name='registration') 
]