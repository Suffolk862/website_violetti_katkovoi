from django.db import models
from django.contrib.auth.models import User

class Test(models.Model):
	quantity_questions = models.SmallIntegerField()
	max_mark = models.SmallIntegerField()

class Question(models.Model):
	test = models.ForeignKey(Test, on_delete=models.CASCADE)
	question = models.TextField(max_length=5000)
	correct_answer = models.SmallIntegerField()
	mark = models.SmallIntegerField()

	def __str__(self):
		return self.question	

class Answer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	test = models.ForeignKey(Test, on_delete=models.CASCADE)
	question = models.OneToOneField(Question, on_delete=models.CASCADE)
	ANSWERS = (
		(1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
	)
	answer = models.SmallIntegerField(choices=ANSWERS)
	user_mark = models.SmallIntegerField()

	def appoints_mark():
		if answer == Test.correct_answer: 
			user_mark = Test.mark
		else:
			user_mark = 0





