from rest_framework import fields, routers, serializers,viewsets 
from django.db import models
from GrupoChat.models import Chat

class ChatSerializer(serializers.ModelSerializer): 
    class Meta :
        model = Chat
        fields = ('user','name','descripcion')