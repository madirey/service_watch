from django.db import models
from django.contrib.auth.models import User
class Sower(models.model):
	user = models.ForeignKey(User)
	description = models.CharField(limit=1000)
	rating = RatingField(range=5)

class Grower(models.model):
	user = models.ForeignKey(User)
	rating = RatingField(range=5)
class Task(models.model):
	title = models.CharField(limit=40)
	description = models.CharField(limit=400)
	time = DateTimeField()
	#tags
