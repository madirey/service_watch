from django.db import models
from django.contrib.auth.models import User
from djangoratings.fields import RatingField

class Sower(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=40, default="You need a title")
	description = models.CharField(max_length=1000)
	rating = RatingField(range=5)

	def __unicode__(self):
		return self.title

class Grower(models.Model):
	user = models.ForeignKey(User)
	rating = RatingField(range=5)

	def __unicode__(self):
		return self.user

class Task(models.Model):
	title = models.CharField(max_length=40)
	description = models.CharField(max_length=400)
	address = models.CharField(max_length=1000, null=True, blank=True)
	time = models.DateTimeField()

	def __unicode__(self):
		return self.title
