import re
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response

from GrupoChat.models import Chat
from ListaChat.serializer import ListaSerializer
from django.db import connection

from ListaChat.models import ListChat

class ListaParticipante(APIView):

    def busquedaChat(self,id):
        try:
            return Chat.objects.get(pk=id)
        except Chat.DoesNotExist:
            return 404

    def post (self,request,format=None):
        id = request.data['chat']
        idChats = self.busquedaChat(id)

        if idChats == 404:
            return Response("no se encontro el usuario")
        else : 
            print(":)")
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM "ListChat" WHERE  chat_id=%s and user_id=%s',[request.data['chat'],request.data['user'] ])  
            consulta = cursor.fetchall()
            if consulta:
                return Response("ya se creo ese usuario")
            else: 
                serializers = ListaSerializer(data = request.data)
                if serializers.is_valid():
                    serializers.save()
                    return Response("ya se agrego")
                else: 
                    return Response("no se creo")

class VerParticipante (APIView):

    def busquedaChat(self,id):
        try:
            return Chat.objects.get(pk=id)
        except Chat.DoesNotExist:
            return 404
    
    def post (self,request,format=None):
        id = request.data['chat']
        idChats = self.busquedaChat(id)
        if idChats == 404:
            return Response("no se encontro el usuario")
        else : 
            print(":) UmU")
            cursor = connection.cursor()
            cursor.execute('SELECT "ListChat".id,first_name, last_name,photo FROM public."ListChat" inner join auth_user on '+
            '"ListChat".user_id = auth_user.id  inner join "Profile" on "Profile".user_id = auth_user.id '+
            'where  "ListChat".chat_id = %s',[int(id)])  
            consulta = cursor.fetchall()
            if consulta:
                dato = []
                for i in consulta:
                    dato.append({'id':i[0],'first_name':i[1],"last_name":i[2],"photo":i[3]})
                
                return Response(dato)
            else:
                return Response("error")
    

class DeleteParticipante (APIView): 

    def busquedaUsuario(self,id):
        try:
            return ListChat.objects.get(pk=id)
        except ListChat.DoesNotExist:
            return 404
    
    def delete(self,request,id,format=None):
        idParticipante = self.busquedaUsuario(id)
        if idParticipante == 404:
            return Response("usuario no encontrado")
        else: 
            idParticipante.delete()
            cursor = connection.cursor()
            cursor.execute('select * from "ListChat"  where id= %s',[id]) 
            consulta = cursor.fetchall()
            if consulta:
                print(":)")
                return Response("no se pudo eliminar ")
            else:
                print(":(")
                return Response("ya se pudo eliminar")