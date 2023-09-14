from rest_framework import serializers
from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Users
        fields = '__ALL__'
        
class EquipamentosSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Equipamentos
        fields = '__ALL__'
        
class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Comentarios
        fields = '__ALL__'
        
class RelacaoSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Relacao
        fields = '__ALL__'