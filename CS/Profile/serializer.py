from rest_framework import fields, routers, serializers,viewsets 
from django.contrib.auth.models import User
from Profile.models import Profile

class RegistroSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = ('username','email','password')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class ProfilesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')