from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm, ProfileForm
from .models import Profile


def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('main:index'))


def registration(request):
	if request.method != 'POST':
		user_form = RegistrationForm()
		profile_form = ProfileForm()
	else:
		user_form = RegistrationForm(data=request.POST)
		profile_form = ProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			new_user = user_form.save()

			new_profile = Profile(language=profile_form.cleaned_data['language'], user_id=new_user.id)
			new_profile.save()

			authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('tests:test'))

	context = {'user_form': user_form, 'profile_form': profile_form}
	return render(request, 'users/registration.html', context)
