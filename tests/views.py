from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import modelformset_factory
from .models import Test, Question, Answer
from .forms import AnswerFormSet


def test(request):
	"""Test"""
	if request.method != 'POST':
		# Пустая форма
		formset = AnswerFormSet()
		questions = Question.objects.filter(test=1)

		fullset = zip(questions, formset)
		context = {'fullset': fullset}
		return render(request, 'tests/test.html', context)
	else:
		# Обработка заполненной формы.
		data = {
			'form-TOTAL_FORMS': '6',
			'form-INITIAL_FORMS': '0',
			'form-MAX_NUM_FORMS': '6',
			}
		formset = AnswerFormSet(request.POST)
		print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		print(formset)
		print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		if formset.is_valid():
			print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
			answer=formset.cleaned_data
			print(answer)
			print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
			formset.save()
		return HttpResponseRedirect(reverse('main:index'))

		return render(request, 'tests/test.html')
