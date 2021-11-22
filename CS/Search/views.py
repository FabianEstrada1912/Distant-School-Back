from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db import connection

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
                    data.append({"id":i[0],"username":i[1],"first_name":i[2],"last_name":i[3]})
                return Response(data)
            else:
                return Response("no se encontro")