from django.db import models
from django.db import timezone

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=200, null=False)
    senha = models.DecimalField(max_digits=30, decimal_places=2, null=False)
    cargo = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.name
    
class Equipamentos(models.Model):
    name = models.CharField(max_length=200, null=False)
    descricao = models.CharField(max_length=500, null=False)
    foto = models.CharField(max_length=500, null=False)
    data = models.DateTimeField(default=timezone.now())
    status = models.BooleanField()
    
    def __str__(self):
        return self.name
    
class Comentarios(models.Model):
    users = models.ForeignKey(Users, related_name="users", on_delete=models.CASCADE)
    comentario = models.CharField(max_length=500, null=False)
    data = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.name
    
class Relacao (models.Model):
    equipamento = models.ForeignKeyForeignKey(Equipamentos, related_name="equipamento", on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentarios, related_name="comentario", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
