from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include
from Profile import views

urlpatterns = [
    re_path(r'Registro/',views.Profiles.as_view()),
    re_path(r'Profile/(?P<id>\d+)/(?P<idUser>\d+)/$',views.ProfileLS.as_view()),
]