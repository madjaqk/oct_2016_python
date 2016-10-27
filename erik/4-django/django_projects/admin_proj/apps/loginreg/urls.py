from django.conf.urls import url
from django.contrib import admin
from . import views
#loginreg
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^login$',views.login,name='login'),
    url(r'^logout$',views.logout,name='logout'),
    url(r'^registration$',views.registration,name='register')
]