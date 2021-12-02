from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include
from GrupoChat import views

urlpatterns = [
    re_path(r'Chat/',views.Grupos.as_view()),
    re_path(r'Ver/',views.Ver.as_view()),
]