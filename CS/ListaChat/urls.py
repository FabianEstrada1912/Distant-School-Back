from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include

from ListaChat import views

urlpatterns = [
    re_path(r'Registro/',views.ListaParticipante.as_view()),
    re_path(r'Ver/',views.VerParticipante.as_view()),
    re_path(r'Eliminar/(?P<id>\d+)/$',views.DeleteParticipante.as_view()),
]