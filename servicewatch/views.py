from django.shortcuts import render_to_response
from django.template import RequestContext
from servicewatch.models import Sower 

def sower_profile(request, id):
	return render_to_response('Sower.html', { 'sower': Sower.objects.get(id) },
			context_instance=RequestContext(request))
