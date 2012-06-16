from tastypie.resources import ModelResource
from servicewatch.models import Sower, Grower, Task

class SowerResource(ModelResource):
	class Meta:
		queryset = Sower.objects.all()

class GrowerResource(ModelResource):
	class Meta:
		queryset = Grower.objects.all()

class TaskResource(ModelResource):
	class Meta:
		queryset = Task.objects.all()

