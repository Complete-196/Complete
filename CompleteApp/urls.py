from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addNew/$', views.addview),
    url(r'^delete/(?P<id>[\w-]+)/$',views.delete, name='delete'),
    url(r'^edit/(?P<id>[\w-]+)/$',views.edit, name='edit'),
    url(r'^password/$', views.password, name='password'),
]