from django.conf.urls import url, include
from extract_skill import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^extract_skill/$', views.SnippetList.as_view()),
    url(r'^extract_skill/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^$', views.api_root),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)