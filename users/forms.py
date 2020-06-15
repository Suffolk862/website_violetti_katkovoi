from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class RegistrationForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
		labels = {
			'first_name': 'имя',
			'last_name': 'фамилия',
			'email': 'email'
		}


class ProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ['language']
		labels = {
			'language': 'язык'
		}
