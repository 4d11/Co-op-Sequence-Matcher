from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
	"""
	SEQUENCES = (
		('1','Sequence 1'),
		('2','Sequence 2'),
		('3','Sequence 3'),
		('4','Sequence 4'),
	)
	"""
	email = models.EmailField
	current_sequence = models.IntegerField
	desired_sequence = models.IntegerField

	def __repr__(self):
		return self.email
