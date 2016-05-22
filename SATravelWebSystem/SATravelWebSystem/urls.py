"""SATravelWebSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from HomePage import views as Home_Views
from ListPage import views as List_Views
from TripPage import views as Trip_Views
from GuidePage import views as Guide_Views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home_Views.home, name='home'),
    url(r'^signin', Home_Views.signin, name='signin'),
    url(r'^login', Home_Views.login, name='login'),
    url(r'^finish', Home_Views.finish, name='finish'),
    url(r'^finally', Home_Views.login_finish, name='finally'),
    url(r'^list', List_Views.list, name='list'),
    url(r'^trip', Trip_Views.trip, name='trip'),
    url(r'^guide', Guide_Views.guide, name='guide'),
]
