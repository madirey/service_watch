from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from servicewatch import models
admin.autodiscover()
admin.site.register(models.Sower)
admin.site.register(models.Grower)
admin.site.register(models.Task)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'servicewatch.views.home', name='home'),
    # url(r'^servicewatch/', include('servicewatch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
