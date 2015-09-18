from django.conf.urls import patterns, url

urlpatterns = patterns('imageview.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^$', 'list', name='rootlist'),
)