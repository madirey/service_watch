from tastypie.resources import ModelResource
from servicewatch.models import Sower

class SowerResource(ModelResource):
	class Meta:
		queryset = Sower.objects.all()

