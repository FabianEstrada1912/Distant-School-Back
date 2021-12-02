
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection

from Conversacion.serializer import ConSerializer

class Conversacion(APIView):

    def get(self,request,format=None):
        return Response("no tienes acceso")
    
    def post(self,request,format=None):
        seria = ConSerializer(data=request.data)
        if seria.is_valid():
            seria.save()
            dato= seria.data
            return Response(dato)
        else:
            return Response("no se creo")

class ConversacionVer(APIView):
    def get(self,request,id,idU,format=None):
        cursor = connection.cursor()
        cursor.execute('SELECT id,sender_id, receiver, mensaje, created FROM "Conversacion" '+ 
            'WHERE sender_id=%s and receiver=%s',[str(id),str(idU)])  
        consulta = cursor.fetchall()
        if consulta:
            datos = []
            for i in consulta:
                datos.append({"id":i[0],"sender":i[1],"receiver":i[2],"mensaje":i[3],"created":i[4]})
            
            cursor.execute('SELECT id,sender_id, receiver, mensaje, created FROM "Conversacion" '+ 
            'WHERE sender_id=%s and receiver=%s',[str(idU),str(id)])  
            consultaR = cursor.fetchall()
            if consultaR:
                dato = []
                for i in consultaR:
                    dato.append({"id":i[0],"sender":i[1],"receiver":i[2],"mensaje":i[3],"created":i[4]})
                
                cursor.execute('SELECT id, archivo, created FROM "Conversacion" '+ 
                    'WHERE sender_id=%s and receiver=%s and archivo !=null;',[str(id),str(idU)])  
                consultaArchivo = cursor.fetchall()
                if consultaArchivo:
                    datoArchivo = []
                    for i in consultaArchivo:
                        datoArchivo.append({"id":i[0],"archivo":i[1],"created":i[2],"receptor":1})

                    cursor.execute('SELECT id, archivo, created FROM "Conversacion" '+ 
                    'WHERE sender_id=%s and receiver=%s and archivo !=null;',[str(idU),str(id)])  
                    consultaArchivoEmisor = cursor.fetchall()

                    if consultaArchivoEmisor:
                        datoArchivoEmisor = []
                        for i in consultaArchivoEmisor:
                            datoArchivoEmisor.append({"id":i[0],"archivo":i[1],"created":i[2],"emisor":2})
                        return Response({"receptor":datos,"remite":dato,"archivoReceptor":datoArchivo,"archivoEmisor":datoArchivoEmisor})
                    else:
                        return Response({"receptor":datos,"remite":dato,"archivoReceptor":datoArchivo})
                else:
                    return Response({"receptor":datos,"remite":dato})
            else:
                return Response(datos)
        else: 
            return Response("no hay conversacion")
