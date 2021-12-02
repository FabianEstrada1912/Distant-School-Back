from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include
from Conversacion import views

urlpatterns = [
    re_path(r'Conversacion/',views.Conversacion.as_view()),
    re_path(r'ConversacionVer/(?P<id>\d+)/(?P<idU>\d+)/$',views.ConversacionVer.as_view()),
]