from rest_framework import serializers
from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Users
        fields = '__all__'
        
class EquipamentosSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Equipamentos
        fields = '__all__'
        
class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Comentarios
        fields = '__all__'
        
class RelacaoSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Relacao
        fields = '__all__'