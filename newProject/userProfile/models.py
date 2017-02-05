from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length=6)
	mobile = models.IntegerField(null=True)
	address = models.TextField()	
	boardX = models.CharField(max_length=10)
	streamX = models.CharField(max_length=10)
	marksX = models.IntegerField(null=True)
	yearX = models.IntegerField(null=True)	
	boardXII = models.CharField(max_length=10)
	streamXII = models.CharField(max_length=10)
	marksXII = models.IntegerField(null=True)
	yearXII = models.IntegerField(null=True)
	college = models.CharField(max_length=10)
	course = models.CharField(max_length=10)
	cgpa = models.IntegerField(null=True)
	gradYear = models.IntegerField(null=True)

	def __str__(self):
		return self.name

class ExtraCurricularActivity(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	activityName = models.CharField(max_length=50)
	year = models.IntegerField()
	participationOrAward = models.CharField(max_length=150)
