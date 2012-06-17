from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from servicewatch.models import Sower 

def home(request):
	return render_to_response('Home.html', { },
			context_instance=RequestContext(request))

def sower_profile(request, id):
	return render_to_response('Sower.html', { 'sower': Sower.objects.get(id=id) },
			context_instance=RequestContext(request))

def image_redirect(request, path):
	return redirect('/static/img/%s' % path)
