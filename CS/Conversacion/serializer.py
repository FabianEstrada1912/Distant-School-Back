from rest_framework import fields, routers, serializers,viewsets 
from django.db import models
from Conversacion.models import Conversacion

class ConSerializer(serializers.ModelSerializer):
    class Meta:
        models = Conversacion
        fields = ('sender','receiver','mensaje')