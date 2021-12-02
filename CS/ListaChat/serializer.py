from rest_framework import fields, routers, serializers,viewsets 
from django.db import models
from ListaChat.models import ListChat

class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListChat
        fields = ('user','chat')