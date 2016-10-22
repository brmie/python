from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.main, name='main'),
	url(r'^list/(?P<nowPage>[0-9]+)/$', views.post_list, name='post_list'),
	url(r'^post/(?P<nowPage>[0-9]+)/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/(?P<nowPage>[0-9]+)/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<nowPage>[0-9]+)/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<nowPage>[0-9]+)/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
]