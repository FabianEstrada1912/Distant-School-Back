from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from FriendUser.models import Friend
from django.contrib.auth.models import User

from django.db import connection
from FriendUser.models import Friend

class Search(APIView):
    
    def get(self,request):
        return Response("No tienes acceso")
    
    def post(self,request,format=None):

        datos = request.data['username']
        if datos == "":
            print("esta vacio")
            return Response("lo siento no hay datos")
        else:
            print("si hay datos")
            cursor = connection.cursor()
            
            cursor.execute('SELECT id,username, first_name, last_name FROM auth_user '+
                        'where username=%s or first_name=%s or last_name=%s',[datos,datos,datos])  
            consulta = cursor.fetchall()
            if consulta:
                data = []
                for i in consulta:
                    cursor.execute('select * from "Profile" inner join auth_user on '+
                        '"Profile".user_id = auth_user.id Where "Profile".user_id= %s',[str(i[0])] )  
                    consultaProfile = cursor.fetchall()
                    for j in consultaProfile:
                        data.append({"id":i[0],"username":i[1],"first_name":i[2],"last_name":i[3],'photo':j[3]})
                return Response(data)
            else:
                return Response("no se encontro")


class FriendListVist(APIView):

    def busquedaUsuario(self,id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return 404
    
    def busquedaFriend(self,id):
        try:
            return Friend.objects.get(pk=id)
        except Friend.DoesNotExist:
            return 404

    def get(self,request,id,idFriend,form=None):
        idUser = self.busquedaUsuario(id)
        idF = self.busquedaFriend(idFriend)
        if idUser == 404 and idF == 404:
            return Response("usuario no encontrado")
        else:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM "Friend" inner join auth_user on '+ 
               '"Friend".user_id = auth_user.id WHERE "Friend".user_id=%s and "idFriends"=%s',[int(id),str(idFriend)])  
            consulta = cursor.fetchall()
            if consulta:
                dato = {}
                dato = {'idFriend':consulta[0][1],'check':consulta[0][3],'user_id':consulta[0][4]}
                return Response(dato)
            else: 
                return Response("no se encontro")