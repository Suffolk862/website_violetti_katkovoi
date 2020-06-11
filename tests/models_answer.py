class Answer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	test = models.OneToOneField(Test, on_delete=models.CASCADE)
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