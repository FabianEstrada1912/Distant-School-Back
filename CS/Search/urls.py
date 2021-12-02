from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include, url

from Search import views

urlpatterns = [
    re_path(r'Search/',views.Search.as_view()),
    re_path(r'SearchF/(?P<id>\d+)/(?P<idFriend>\d+)/$',views.FriendListVist.as_view()),
]