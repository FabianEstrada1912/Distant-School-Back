from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response

from FriendUser.serializer import FriendsEditSerializer
from FriendUser.serializer import FriendsSerializer
from django.db import connection
from FriendUser.models import Friend
from django.contrib.auth.models import User

class Frieds(APIView):
    
    def get(self,request):
        return Response("No tienes acceso")

    def post(self,request,format=None):

        friends = {
            'user':request.data['user'],
            'idFriends':request.data['idFriends'],
        }
        print(friends)
        serializer = FriendsEditSerializer(data = request.data)
        print(serializer)
        if serializer.is_valid():
            print("yupi")
            user = serializer.save()
            return Response ("se creo el usuario")
        else :
            return Response ("no se creo el usuario :(")

class FriendVist(APIView):

    def busquedaUsuario(self,id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return 404
    
    def busquedaFriend(self,id):
        try:
            return Friend.objects.get(pk=id)
        except User.DoesNotExist:
            return 404

    def post(self,request,id,form=None):
       
        idUser = self.busquedaUsuario(id)
        if idUser == 404:
            return Response("usuario no encontrado")
        else: 
            check = request.data['check']
             # 1 es agregado  y 0 es no agregado
            cursor = connection.cursor()
            
            cursor.execute('SELECT user_id,"idFriends", "check",id '+
                'FROM "Friend" WHERE user_id = %s and "check" = %s ',[id,str(check) ])  
            consulta = cursor.fetchall()
            if consulta:
                lista = []
                lista = self.proces(consulta)
                return Response(lista)
            else:
                return Response("no se encontro") 
    
    def proces(self,consulta):
        data = []
        for i in consulta:
            data.append({"idUser":i[0],"idFriends":i[1],"check":i[2],'id':i[3]})
                
        lista = []
        for i in data:
            user = str(i['idFriends'])
            ids = i['id']
            cursor = connection.cursor()
            cursor.execute('select id,username, first_name, last_name from auth_user Where auth_user.id = %s',[user])  
            consulta = cursor.fetchall()
            if consulta:
                cursor.execute('select * from "Profile" inner join auth_user on '+
                        '"Profile".user_id = auth_user.id Where "Profile".user_id= %s',[user])  
                consultaProfile = cursor.fetchall()
                for i in consulta:
                    for j in consultaProfile:
                        lista.append({'id':i[0],'username':i[1],'first_name':i[2],'last_name':i[3],'photo':j[3],'idF':ids})
            

        return lista
    
    def put(self,request,id,format=None):
        idUser = self.busquedaUsuario(id)
        if idUser == 404:
            return Response("usuario no encontrado")
        else: 
            idFriend = request.data['idFriends']
            cursor = connection.cursor()
            
            cursor.execute('SELECT id,user_id,"idFriends","check" '+ 
                'FROM "Friend" WHERE user_id = %s and "idFriends" = %s ',[id,str(idFriend)])  

            consulta = cursor.fetchall()
            if consulta:
                idList = 0
                for i in consulta:
                    idList = i[0]
                
                cursor.execute('UPDATE "Friend" SET "idFriends" = %s,"check"= %s  WHERE id=%s',[request.data['idFriends'],request.data['check'],int(idList) ])
                
                cursor.execute('SELECT user_id,"idFriends", "check" '+
                'FROM "Friend" WHERE user_id = %s or "check" = %s ',[idList,str(request.data['check'])])  
                consulta = cursor.fetchall()
                if consulta:
                    print(":)")
                    return Response("ya se pudo editar")
                else:
                    print(":(")
                    return Response("no se pudo editar")
                
            else:
                return Response("no se encontro")
    
    def delete(self,request,id,format=None):
        idUser = self.busquedaFriend(id)
        if idUser == 404:
            return Response("usuario no encontrado")
        else: 
            idUser.delete()
            cursor = connection.cursor()
            cursor.execute('SELECT user_id,"idFriends", "check" '+
                'FROM "Friend" WHERE id = %s',[str(idUser)])  
            consulta = cursor.fetchall()
            if consulta:
                print(":)")
                return Response("no se pudo eliminar ")
            else:
                print(":(")
                return Response("ya se pudo eliminar")