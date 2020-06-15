from django import forms
from django.forms import ModelForm, modelformset_factory
from .models import Answer


class AnswerForm(forms.ModelForm):

	class Meta:
		model = Answer
		fields = ['answer']
		labels = {
			'answer': 'выберите вариант ответа:',
		}


AnswerFormSet = modelformset_factory(Answer, form=AnswerForm, extra=6)
