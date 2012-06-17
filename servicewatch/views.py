from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from servicewatch.models import Grower, Sower, Task

def home(request):
	return render_to_response('Home.html', { },
			context_instance=RequestContext(request))

def sower_profile(request, id):
	return render_to_response('Sower.html', { 'sower': Sower.objects.get(id=id) },
			context_instance=RequestContext(request))

def grower_profile(request, id):
	return render_to_response('Grower.html', { 'grower': Grower.objects.get(id=id) },
			context_instance=RequestContext(request))

def image_redirect(request, path):
	return redirect('/static/img/%s' % path)

def user_survey(request):
	return render_to_response('UserSurvey.html', { },
			context_instance=RequestContext(request))

def org_survey(request):
	return render_to_response('OrgSurvey.html', { },
			context_instance=RequestContext(request))

def task_profile(request, id):
	return render_to_response('Task.html', { 'task': Task.objects.get(id=id) },
			context_instance=RequestContext(request))

def notifications(request):
	return render_to_response('Notifications.html', { 'tasks': Task.objects.all() }, 
			context_instance=RequestContext(request))

def search(request):
	return render_to_response('Search.html', { },
			context_instance=RequestContext(request))
