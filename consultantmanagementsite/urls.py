from django.conf.urls import patterns, include, url

from consultantmapp.views import consultant_list
from consultantmapp.views import search_form
from consultantmapp import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'consultantmanagement.views.home', name='home'),
    # url(r'^consultantmanagement/', include('consultantmanagement.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^consultant/$',consultant_list),
    url(r'^search-form/$', search_form),
    url(r'^consultant/(?P<consultant_id>\d+)/$', views.consultant_view)
)
