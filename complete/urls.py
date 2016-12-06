"""complete URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm

from login.views import *
from django.contrib.auth import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^CompleteApp/', include('CompleteApp.urls')),
    url(r'^$', views.login),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', views.login, name='login'),  # If user is not login it will redirect to login page
    url(r'^accounts/logout/$', views.logout, {'next_page' : '/accounts/login'}),
    url(r'^register/$', register, name='register'),
    url(r'^forgot/$', password_reset, {"template_name":"registration/login.html", "subject_template_name":"registration/subject_name.txt"}, name= 'forgot'),
    url(r'^forgot/passwordsent/$', password_reset_done, {"template_name":"registration/confirm.html"}, name='password_reset_done'),
    url(r'^forgot/passwordconfirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {"template_name":"registration/confirm.html"}, name='password_reset_confirm'),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
]