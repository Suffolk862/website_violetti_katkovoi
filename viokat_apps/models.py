from django.db import models

class Task(models.Model):
	"""Task for student"""
	text = models.TextField(max_length=2000)
	date_added = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.text