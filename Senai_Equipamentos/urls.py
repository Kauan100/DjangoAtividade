from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #estamos criando a rota/endpoint de acesso à API!
    path("users/", UsersAPIView.as_view(), name='users'),
    path("users/<int:id>", UsersAPIView.as_view(), name='usersParameter'),
    path("equipamentos/", EquipamentosAPIView.as_view(), name='equipamentos'),
    path("equipamentos/<int:id>", EquipamentosAPIView.as_view(), name='equipamentosParameter'),
    path("comentarios/", ComentariosAPIView.as_view(), name='comentarios'),    
    path("comentarios/<int:id>", ComentariosAPIView.as_view(), name='comentariosParameter'),
    path("relacao/", RelacaoAPIView.as_view(), name='relacao'),
    path("relacao/<int:id>", RelacaoAPIView.as_view(), name='relacaoParameter'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]