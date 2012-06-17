from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from servicewatch import models, views
from servicewatch.api import SowerResource, GrowerResource, TaskResource
from servicewatch import admin as sw_admin
from tastypie.api import Api

admin.autodiscover()
admin.site.register(models.Sower)
admin.site.register(models.Tag)
admin.site.register(models.Task)

v1_api = Api(api_name='v1')
v1_api.register(SowerResource())
v1_api.register(GrowerResource())
v1_api.register(TaskResource())

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home), 
    # url(r'^servicewatch/', include('servicewatch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^comments/', include('django.contrib.comments.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^api/', include(v1_api.urls)),
	url(r'^sower/(?P<id>\d+)', views.sower_profile),
    url(r'^grower/(?P<id>\d+)', views.grower_profile),
    url(r'^task/(?P<id>\d+)', views.task_profile),
    url(r'^rating', views.sower_profile),
    url(r'^sower/img/(?P<path>.+)', views.image_redirect),
)

urlpatterns += staticfiles_urlpatterns()
