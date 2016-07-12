from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Create your models here.

class Sub(models.Model):
	num = models.IntegerField()
	name = models.CharField(max_length=100)
	my = models.IntegerField()
	ev1 = models.IntegerField()
	ev2 = models.IntegerField()

	
	def __str__(self):
		return self.name

