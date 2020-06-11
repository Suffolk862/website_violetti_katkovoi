from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	LANGUAGES = (
		('English', 'English'),
        ('French', 'French'),
	)
	language = models.CharField(max_length=7, choices=LANGUAGES, help_text='выберите язык, который хотите изучать.')




