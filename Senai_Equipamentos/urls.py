from django.urls import path
from .views import *

urlpatterns = [
    #estamos criando a rota/endpoint de acesso à API!
    path("character/", UsersAPIView.as_view(), name='users'),
    path("character/<int:id>", UsersAPIView.as_view(), name='usersParameter'),
    path("location/", EquipamentosAPIView.as_view(), name='equipamentos'),
    path("location/<int:id>", EquipamentosAPIView.as_view(), name='equipamentosParameter'),
    path("episode/", ComentariosAPIView.as_view(), name='comentarios'),    
    path("episode/<int:id>", ComentariosAPIView.as_view(), name='comentariosParameter'),
    path("character/", RelacaoAPIView.as_view(), name='relacao'),
    path("character/<int:id>", RelacaoAPIView.as_view(), name='relacaoParameter'),
]