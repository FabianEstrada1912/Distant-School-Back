from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.http import Http404
from django.shortcuts import get_object_or_404

import time
from django.http import HttpResponsePermanentRedirect
from django.contrib.auth import login as login_django
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.views import APIView

class Login(ObtainAuthToken,APIView):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class( data = request.data,
                                            context = {
                                                'request':request
                                            })
        if serializer.is_valid():
           print(":)")
           times = time.strftime("%d/%m/%y")
           print (times)
           serializer.is_valid(raise_exception = True)
           user = serializer.validated_data['user']
           token, created = Token.objects.get_or_create(user=user)
           
           return Response({
                'token':token.key,
                'user_id':user.pk, 
                'username':user.username,
                'first_name':user.first_name,
                'last_name':user.last_name,
                'email':user.email,
            })
           
        else:
           print(":(")
           return Response('usuario no valido')