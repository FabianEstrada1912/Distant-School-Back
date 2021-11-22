from rest_framework import fields, routers, serializers,viewsets 
from django.db import models
from FriendUser.models import Friend

class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('idFriends','check')

class FriendsEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('user','idFriends','check')
        
 