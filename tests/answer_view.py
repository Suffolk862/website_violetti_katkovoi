	if answer_form.is_valid():
			n = 0	
			while n != 10:
				n = n+1
				test_id = Test.objects.get(pk=n)				
				answer_model = Answer(test_id=test_id.id, answer=answer_form.cleaned_data['answer'])
				answer_model.save()
