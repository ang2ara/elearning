#from django.conf.urls import include, url
#from django.contrib import admin

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'nusa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name='elearning/index.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='elearning/profile.html')),
]
