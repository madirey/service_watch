from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from servicewatch import models
from servicewatch.api import SowerResource
from tastypie.api import Api

admin.autodiscover()
admin.site.register(models.Sower)
admin.site.register(models.Grower)
admin.site.register(models.Task)

v1_api = Api(api_name='v1')
v1_api.register(SowerResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'servicewatch.views.home', name='home'),
    # url(r'^servicewatch/', include('servicewatch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^api/', include(v1_api.urls)),
)
