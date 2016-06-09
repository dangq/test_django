from django.conf.urls import url

from predict import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
	url(r'^test/$', views.test, name='test'),
	# url(r'^profile/$', views.profile, name='profile'),
	# url(r'^model/$', views.model, name='model'),
	url(r'^movement/$', views.movement, name='movement'),
    url(r'^list$', views.list, name='list'),
]
