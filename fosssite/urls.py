from django.conf.urls import url
from . import views
from django.conf.urls import patterns, url


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^signup/$', views.UserFormView, name='UserFormView'),
	url(r'^login/$',views.login,name='login'),
	url(r'^auth/$',views.auth_view,name='auth_view'),
	url(r'^profileuser/$',views.profileuser,name='profileuser'),
	url(r'^profileuser/edit/$', views.post_edit, name='post_edit'),
]
