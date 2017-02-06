from django.conf.urls import url

from . import views

urlpatterns = [
				url(r'^$', views.showForm, name='showForm'),
				url(r'^save/$', views.save, name='save')
				]