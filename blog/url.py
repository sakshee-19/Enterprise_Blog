from django.conf.urls import url
from blog import views as blog_view

urlpatterns = [
    url(r'^$', blog_view.post_list, name='post_list'),
    url(r'^post_create/$', blog_view.post_create, name='post_create'),
    url(r'^post_detail/(?P<slug>[\w-]+)/$', blog_view.post_detail, name='post_detail'),
    url(r'^post_update/(?P<slug>[\w-]+)/$', blog_view.post_update, name='post_update'),
    url(r'^post_delete/(?P<slug>[\w-]+)/$', blog_view.post_delete, name='post_delete')
]