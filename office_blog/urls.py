from django.conf.urls import url,include
from office_blog.views import IndexView,detail,ArchivesViews,CategoryViews,tag,search


app_name = 'office_blog'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    #url(r'^index/$', index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})$', ArchivesViews.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', CategoryViews.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', tag, name='tag'),
    url(r'^search/$', search, name='search'),
]