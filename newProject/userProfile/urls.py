from django.conf.urls import url
from . import views

app_name = "user"
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'(?P<userID>[0-9]+)/editprofile', views.editProfile, name = 'editProfile'),
	url(r'^(?P<userID>[0-9]+)/save/$', views.save, name= 'save')
]