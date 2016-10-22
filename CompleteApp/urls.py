from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addNew/$', views.addview),
    url(r'^delete/(?P<id>[0-9]+)/$',views.delete, name='delete'),
]