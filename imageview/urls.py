from django.conf.urls import patterns, url
from .views import UploadView, MainView

urlpatterns = patterns('imageview.views',
                       url(r'^upload/$', UploadView.as_view(), name='upload'),
                       url(r'^$', MainView.as_view(), name='rootlist'),
                       )
