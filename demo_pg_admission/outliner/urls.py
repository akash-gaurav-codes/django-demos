from django.conf.urls import url

from . import views

urlpatterns = [
				url(r'^$', views.entryList, name='entryList'),
				url(r'^(?P<id>[0-9]+)/$', views.entryDetail, name='entryDetail'),
				url(r'^api/v1/$', views.entryListAPI, name='entryListAPI'),
				url(r'^api/v1/(?P<id>[0-9]+)/$', views.entryDetailAPI, name='entryDetailAPI')
				
				] 