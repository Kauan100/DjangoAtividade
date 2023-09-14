from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from rest_framework import status

# Create your views here.

class UsersAPIView(APIView):
    def post(self, request):
        usersJson = request.data
        usersSerialized = UsersSerializer(data=usersJson)
        usersSerialized.is_valid(raise_exception=True)
        usersSerialized.save()
        return Response(status=201, data=usersSerialized.data)
    
    def get(self, request, UsersId =''):
        if UsersId == '':
            usersFound = Users.objects.all()
            usersSerialized = UsersSerializer(usersFound, many=True)
            return Response(usersSerialized.data)
        else:
            try:
                usersFound = Users.objects.get(id=UsersId)
                usersSerialized = UsersSerializer(usersFound, many=False)
                return Response(usersSerialized.data)
            except Users.DoesNotExist:
                return Response(status=404, data=' Not Found!')
            
    def put(self, request, UsersId = ''):
        usersFound = None
        
        try:
            usersFound = Users.objects.get(id=UsersId)
        except Users.DoesNotExist:
            return Response(status=404,data="People not Found!")
        
        usersJson = request.data
        usersSerialized = UsersSerializer(usersFound, data=usersJson)
        usersSerialized.is_valid(raise_exception=True)
        usersSerialized.save()
        return Response(status=200, data=usersSerialized.data)
    
    def delete(self, request, UsersId = ''):
        usersFound = None
        try:
            usersFound = Users.objects.get(id=UsersId)
        except Users.DoesNotExist:
            return Response(status=404,data="User not Found!")
        usersFound.delete()
        return Response(status=200, data="User successfully deleted!")
    
    
    
class EquipamentosAPIView(APIView):
    def post(self, request):
        equipamentosJson = request.data
        equipamentosSerialized = EquipamentosSerializer(data=equipamentosJson)
        equipamentosSerialized.is_valid(raise_exception=True)
        equipamentosSerialized.save()
        return Response(status=201, data=equipamentosSerialized.data)
    
    def get(self, request, equipamentosId =''):
        if equipamentosId == '':
            equipamentosFound = Equipamentos.objects.all()
            equipamentosSerialized = EquipamentosSerializer(equipamentosFound, many=True)
            return Response(equipamentosSerialized.data)
        else:
            try:
                equipamentosFound = Equipamentos.objects.get(id=equipamentosId)
                equipamentosSerialized = EquipamentosSerializer(equipamentosFound, many=False)
                return Response(equipamentosSerialized.data)
            except Equipamentos.DoesNotExist:
                return Response(status=404, data=' Not Found!')
            
    def put(self, request, equipamentosId = ''):
        equipamentosFound = None
        
        try:
            equipamentosFound = Equipamentos.objects.get(id=equipamentosId)
        except Equipamentos.DoesNotExist:
            return Response(status=404,data="People not Found!")
        
        equipamentosJson = request.data
        equipamentosSerialized = EquipamentosSerializer(equipamentosFound, data=equipamentosJson)
        equipamentosSerialized.is_valid(raise_exception=True)
        equipamentosSerialized.save()
        return Response(status=200, data=equipamentosSerialized.data)
    
    def delete(self, request, equipamentosId = ''):
        equipamentosFound = None
        try:
            equipamentosFound = Equipamentos.objects.get(id=equipamentosId)
        except Equipamentos.DoesNotExist:
            return Response(status=404,data="Equipamento not Found!")
        equipamentosFound.delete()
        return Response(status=200, data="Equipamento successfully deleted!")

            
            
    
class ComentariosAPIView(APIView):
    def post(self, request):
        comentariosJson = request.data
        comentariosSerialized = ComentariosSerializer(data=comentariosJson)
        comentariosSerialized.is_valid(raise_exception=True)
        comentariosSerialized.save()
        return Response(status=201, data=comentariosSerialized.data)
    
    def get(self, request, comentariosId =''):
        if comentariosId == '':
            comentariosFound = Comentarios.objects.all()
            comentariosSerialized = ComentariosSerializer(comentariosFound, many=True)
            return Response(comentariosSerialized.data)
        else:
            try:
                Found = Comentarios.objects.get(id=comentariosId)
                comentariosSerialized = ComentariosSerializer(comentariosFound, many=False)
                return Response(comentariosSerialized.data)
            except Comentarios.DoesNotExist:
                return Response(status=404, data=' Not Found!')
            
    def put(self, request, comentariosId = ''):
        comentariosFound = None
        
        try:
            comentariosFound = Comentarios.objects.get(id=comentariosId)
        except Comentarios.DoesNotExist:
            return Response(status=404,data="People not Found!")
        
        comentariosJson = request.data
        comentariosSerialized = ComentariosSerializer(comentariosFound, data=comentariosJson)
        comentariosSerialized.is_valid(raise_exception=True)
        comentariosSerialized.save()
        return Response(status=200, data=comentariosSerialized.data)
    
    def delete(self, request, comentariosId = ''):
        comentariosFound = None
        try:
            comentariosFound = Comentarios.objects.get(id=comentariosId)
        except Comentarios.DoesNotExist:
            return Response(status=404,data="Comentario not Found!")
        comentariosFound.delete()
        return Response(status=200, data="Comentario successfully deleted!")
            
            
    
class RelacaoAPIView(APIView):
    def post(self, request):
        relacaoJson = request.data
        relacaoSerialized = RelacaoSerializer(data=relacaoJson)
        relacaoSerialized.is_valid(raise_exception=True)
        relacaoSerialized.save()
        return Response(status=201, data=relacaoSerialized.data)
    
    def get(self, request, relacaoId =''):
        if relacaoId == '':
            relacaoFound = Relacao.objects.all()
            relacaoSerialized = RelacaoSerializer(relacaoFound, many=True)
            return Response(relacaoSerialized.data)
        else:
            try:
                Found = Relacao.objects.get(id=relacaoId)
                relacaoSerialized = RelacaoSerializer(relacaoFound, many=False)
                return Response(relacaoSerialized.data)
            except Relacao.DoesNotExist:
                return Response(status=404, data=' Not Found!')
            
    def put(self, request, relacaoId = ''):
        relacaoFound = None
        
        try:
            relacaoFound = Relacao.objects.get(id=relacaoId)
        except Relacao.DoesNotExist:
            return Response(status=404,data="People not Found!")
        
        relacaoJson = request.data
        relacaoSerialized = RelacaoSerializer(relacaoFound, data=relacaoJson)
        relacaoSerialized.is_valid(raise_exception=True)
        relacaoSerialized.save()
        return Response(status=200, data=relacaoSerialized.data)
    
    def delete(self, request, relacaoId = ''):
        relacaoFound = None
        try:
            relacaoFound = Relacao.objects.get(id=relacaoId)
        except Relacao.DoesNotExist:
            return Response(status=404,data="Relacao not Found!")
        relacaoFound.delete()
        return Response(status=200, data="Relacao successfully deleted!")
