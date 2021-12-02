from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from GrupoChat.serializer import ChatSerializer
from GrupoChat.models import Chat
from django.db import connection

class Grupos(APIView):
    
    def busquedaUsuario(self,id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return 404

    def post(self,request,format=None):
        id = request.data['user']
        idUser = self.busquedaUsuario(id)
        if idUser == 404:
            return Response("usuario no encontrado")
        else: 
            serializers = ChatSerializer(data=request.data)
            cursor = connection.cursor()
            if serializers.is_valid():
                print("yupi") 
                serializers.save()
                data= serializers.data
                
                cursor.execute('SELECT  id,name,descripcion,photo,user_id FROM "Chat" WHERE '+
                'user_id=%s and name=%s and descripcion=%s',[request.data['user'],request.data['name'],request.data['descripcion']])  
                consulta = cursor.fetchall()
                grupo = {}
                for i in consulta:
                    grupo = {'id':i[0],'name':i[1],'descripcion':i[2],'photo':i[3],'user_id':i[4]}
                return Response(grupo)
            else : 
                return Response("no se creo")

class Ver(APIView):

    def busquedaUsuario(self,id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return 404

    def post(self,request,format=None):
        id = request.data['user']
        idUser = self.busquedaUsuario(id)
        if idUser == 404:
            return Response("usuario no encontrado")
        else:
            cursor = connection.cursor()
            cursor.execute('SELECT  auth_user.id,"Chat".id,"ListChat".id FROM "ListChat" inner join "Chat" on  "ListChat".chat_id = "Chat".id '+
                'inner join auth_user on "ListChat".user_id = auth_user.id Where auth_user.id=%s',[int(id)])  
            consulta = cursor.fetchall()
            
            if consulta:
                dato = []
                for i in consulta:
                    
                    cursor.execute('select id,name,descripcion,photo,user_id From "Chat" where id=%s',[int(i[1])])
                    consultaG = cursor.fetchall()
                    for j in consultaG:
                        dato.append({'id':j[0],'name':j[1],'descripcion':j[2],'photo':j[3]})
                    
                return Response(dato)
            else:
                return Response("no se encontro")  


class VerGrupo(APIView):
    def busquedaUsuario(self,id):
        try:
            return Chat.objects.get(pk=id)
        except Chat.DoesNotExist:
            return 404

    def post(self,request,format=None):
        id = request.data['id']
        idL = self.busquedaUsuario(id)
        if idL == 404:
            return Response(":(")
        else: 
            cursor = connection.cursor()
            print(id)
            cursor.execute('SELECT  id,name,descripcion,photo,user_id FROM "Chat" WHERE id=%s',[int(id)])  
            consulta = cursor.fetchall()
            if consulta:
                print(":)")
                grupo = {'id':consulta[0][0],'name':consulta[0][1],'descripcion':consulta[0][2],'photo':consulta[0][3],'user_id':consulta[0][4]}
                return Response(grupo)
            else : 
                return Response("no se encontro")