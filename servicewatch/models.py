from django.db import models
from django.contrib.auth.models import User
from djangoratings.fields import RatingField
from taggit.managers import TaggableManager

class Sower(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=40, default="You need a title")
	description = models.CharField(max_length=1000)
	rating = RatingField(range=5)

	def __unicode__(self):
		return self.title

class Tag(models.Model):
	text = models.CharField(max_length=40)

	def __unicode__(self):
		return self.text

class Grower(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=40)
	skills = models.ManyToManyField(Tag, related_name='skills_growers')
	interests = models.ManyToManyField(Tag, related_name='interests_growers')

	rating = RatingField(range=5)

	def __unicode__(self):
		return self.title

class Task(models.Model):
	title = models.CharField(max_length=40)
	description = models.CharField(max_length=400)
	address = models.CharField(max_length=1000, null=True, blank=True)
	time = models.DateTimeField()

	def __unicode__(self):
		return self.title
