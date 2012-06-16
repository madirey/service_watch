from django.db import models
from django.contrib.auth.models import User
from djangoratings.fields import RatingField

class Sower(models.Model):
	user = models.ForeignKey(User)
	description = models.CharField(max_length=1000)
	rating = RatingField(range=5)

class Grower(models.Model):
	user = models.ForeignKey(User)
	rating = RatingField(range=5)
class Task(models.Model):
	title = models.CharField(max_length=40)
	description = models.CharField(max_length=400)
	time = models.DateTimeField()
	#tags
