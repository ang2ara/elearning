from django.conf.urls import include, url
from elearning import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'suvy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^elearning/', include('polls.urls')),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.KursusView.as_view(), name='kursus'),
]
