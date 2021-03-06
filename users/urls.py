from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [#登录页面
	url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
	# 注销
	url(r'^logout/$', views.logout_view, name='logout'),
	# 注册页面
	url(r'^register/$', views.register, name='register'),
	url(r'^setting/$', views.setting, name='setting'),
	url(r'^check_data/$', views.check_data, name='check_data'),
	url(r'^check_pass/$', views.check_pass, name='check_pass'),
]