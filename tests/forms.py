from django import forms
from django.forms import ModelForm, CheckboxInput, modelformset_factory
from .models import Question, Test, Answer

class AnswerForm(forms.ModelForm):

	class Meta:
		model = Answer
		fields = ['answer']
		labels = {
			'answer': 'выберите вариант ответа:',
		}

AnswerFormSet = modelformset_factory(Answer, form=AnswerForm, extra=6)
