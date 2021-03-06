"""NewsFeed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import login, logout

from NewsHub.views import signup, newsfeed
from CLSGGameLogin.views import index, simulation

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'simulations/$', simulation, name='simulation'),
    url(r'^newsfeed/$', newsfeed, name='newsfeed'),
    url(r'^accounts/signup/$', signup, name='signup'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    path('admin/', admin.site.urls),
]
