from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from servicewatch.models import Sower 

def sower_profile(request, id):
	return render_to_response('Sower.html', { 'sower': Sower.objects.get(id=id) },
			context_instance=RequestContext(request))

def grower_profile(request, id):
	return render_to_response('Grower.html', { 'grower': Grower.objects.get(id=id) },
			context_instance=RequestContext(request))

def image_redirect(request, path):
	return redirect('/static/img/%s' % path)