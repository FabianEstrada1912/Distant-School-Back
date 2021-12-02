from rest_framework import fields, routers, serializers,viewsets 
from django.db import models
from Conver.models import Cons

class ConSerializer(serializers.ModelSerializer):
    class Meta:
        models = Cons
        fields = ('sender','receiver','mensaje')