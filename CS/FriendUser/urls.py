from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include, url

from FriendUser import views

urlpatterns = [
    re_path(r'Friends/',views.Frieds.as_view()),
    re_path(r'Friend/(?P<id>\d+)/$',views.FriendVist.as_view()),
    re_path(r'Agregar/(?P<id>\d+)/$',views.AgregarVist.as_view()),
]