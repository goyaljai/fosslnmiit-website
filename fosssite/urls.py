from django.conf.urls import url
from . import views
from django.conf.urls import  url

app_name = 'fosssite'
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^signup/$', views.UserFormView, name='UserFormView'),
<<<<<<< HEAD
	url(r'^login/$',views.login,name='login'),
	url(r'^auth/$',views.auth_view,name='auth_view'),
	url(r'^profileuser/$',views.profileuser,name='profileuser'),
	url(r'^profileuser/edit/$', views.post_edit, name='post_edit'),
=======
	url(r'^login/$',views.login_user,name='login_user'),
	#url(r'^auth/$',views.auth_view,name='auth_view'),
	url(r'^(?P<name>[\w\-]+)$',views.profileuser,name='profileuser'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^(?P<name>[\w\-]+)/editprofile/$',views.edit_user_profile,name='edit_user_profile'),
	url(r'^(?P<name>[\w\-]+)/editprofile/changepassword/$',views.changepassword,name='changepassword'),
	url(r'^events/$',views.events,name='events'),
	url(r'^contributions/$',views.contributions,name='contributions'),
	url(r'^blog/$',views.blog,name='blog'),

>>>>>>> 6c068a332a3c30eba70dad6fe128dd8ac985a811
]
