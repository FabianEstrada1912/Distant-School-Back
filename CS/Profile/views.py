from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status,generics
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.db import connection

from Profile.serializer import RegistroSerializer
from Profile.serializer import ProfilesSerializers
from Profile.serializer import UserSerializer
from Profile.models import Profile
# Create your views here.
class Profiles(ObtainAuthToken,APIView):

    def get(self,request):
        return Response("No tienes acceso :(")
    
    def post(self,request,format=None):
        serializer = RegistroSerializer(data = request.data)
        if serializer.is_valid():
            print("yupi")
            user = serializer.save()
            datas = serializer.data     
            token, created = Token.objects.get_or_create(user=user)
            profiles = Profile(user = user,description ="Welcome")
            profiles.save()
            print(user.id)
            return Response ("se creo el usuario")
        else :
            return Response ("no se creo el usuario :(")

class ProfileLS(APIView):

    def busqueda(self,id):
        try:
            return Profile.objects.get(pk=id)
        except Profile.DoesNotExist:
            return 404
    
    def busquedaUsuario(self,id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return 404

    def put(self,request,id,idUser,format=None):
        id = self.busqueda(id)
        idUser = self.busquedaUsuario(idUser)
        if id == 404 or idUser == 404:
            return Response("no existe ese id")
        else:
     
            profile = {'user':request.data['user'],'description': request.data['description']}
            user = {'username':request.data['username'],'email':request.data['email'],
                   'first_name':request.data['first_name'],'last_name':request.data['last_name']}

            serializer = ProfilesSerializers(id,data=profile)
            serializerUser = UserSerializer(idUser,data=user)

            if serializer.is_valid() and serializerUser.is_valid():
                serializer.save()
                serializerUser.save()
                data = serializer.data
                dataUser = serializerUser.data
                datos = {'user':dataUser,'profile':data}
                return Response(datos)
            else: 
                return Response("No se pudo editar :(")
            
    def get(self,request,id,idUser,format=None):
        id= self.busquedaUsuario(idUser)
        print(id)
        if id == 404:
            return Response("no existe ese id")
        else:
            user = str(id)
            cursor = connection.cursor()
            cursor.execute('select * from "Profile" inner join auth_user on '+
                        '"Profile".user_id = auth_user.id Where username = %s',[user])  
            consulta = cursor.fetchall()
            if consulta:
                data = {}
                for i in consulta:
                    data = {'id':i[0],'descripcion':i[1],'idUser':i[2],'photo':i[3]}
               
                return Response(data)
            else:
                return Response("no se encontro")