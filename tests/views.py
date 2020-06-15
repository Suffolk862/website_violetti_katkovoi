from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question
from .forms import AnswerFormSet


def test(request):
	if request.method != 'POST':
		formset = AnswerFormSet()
		questions = Question.objects.filter(test=1)

		fullset = zip(questions, formset)
		context = {'fullset': fullset}

		return render(request, 'tests/test.html', context)
	else:

		data = {
			'form-TOTAL_FORMS': '6',
			'form-INITIAL_FORMS': '0',
			'form-MAX_NUM_FORMS': '6',
			}
		formset = AnswerFormSet(data, request.POST)

		if formset.is_valid():
			formset.save()
		return HttpResponseRedirect(reverse('main:index'))

		return render(request, 'tests/test.html')
