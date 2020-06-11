from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, ProfileForm
from .models import Profile

from django.contrib.auth.models import User

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('main:index'))

def registration(request):
	"""Регистрирует нового пользователя."""
	if request.method != 'POST':
	# Display blank registration form.
		print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		print('GET')
		print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		user_form = RegistrationForm()
		profile_form = ProfileForm()
	else:
		# Обработка заполненной формы.
		print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		print('POST')
		print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		user_form = RegistrationForm(data=request.POST) # Создание экземпляра данного класса на основе полученных (при помощи метода POST) данных
		profile_form = ProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid(): # проверка того, что данные экземпляра формы не являются вредоносным кодом, а пороли совпадают
			
			new_user = user_form.save()

			new_profile = Profile(language=profile_form.cleaned_data['language'], user_id=new_user.id)
			new_profile.save()

			#profile_form.save()
			# Выполнение входа и перенаправление на домашнюю страницу
			authenticated_user = authenticate(username=new_user.username, password=request.POST['password1']) # метод возвращает объект пользователя, если данные верны
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('tests:test'))
	context = {'user_form': user_form, 'profile_form': profile_form}
	return render(request, 'users/registration.html', context)