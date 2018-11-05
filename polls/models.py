from django.db import models


class Poll(models.Model):
	
	text = models.CharField(max_length=255)
	pub_date = models.DateField()

	def __str__(self):
		return f'{self.text}'

class Choice(models.Model):
	question = models.ForeignKey(Poll, on_delete = models.CASCADE)
	choice_text = models.CharField(max_length=255)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return f'{self.question.text} - {self.choice_text}'