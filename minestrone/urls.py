from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import minestrone.soup.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minestrone.views.home', name='home'),
    # url(r'^minestrone/', include('minestrone.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', minestrone.soup.views.JobsView.as_view()),
    url(r'^jobs/$', minestrone.soup.views.JobsView.as_view()),
    url(r'^editor/$', minestrone.soup.views.EditorView.as_view()),
)
