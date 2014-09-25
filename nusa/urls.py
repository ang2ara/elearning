#from django.conf.urls import include, url
#from django.contrib import admin

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from elearning import views

admin.autodiscover()

urlpatterns = [
     # ex: /index/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # register seluruh url yang ada di dalam model elearning
    url(r'^elearning/', include('elearning.urls', namespace ='elearning')),

    # register seluruh url yang ada di dalam model admin
    url(r'^admin/', include(admin.site.urls)),

    # register seluruh url yang ada di dalam model allauth
    url(r'^accounts/', include('allauth.urls')),

    # url profile
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='elearning/profile.html')),
]
