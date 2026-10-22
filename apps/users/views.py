from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Usuario, Perfil
from .serializers import UsuarioSerializer, UsuarioMeSerializer, PerfilSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Adiciona dados do usuário no response do login."""

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['nome'] = user.nome
        token['perfil'] = user.perfil.descricao
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = {
            'email': self.user.email,
            'nome': self.user.nome,
            'perfil': self.user.perfil.descricao,
            'is_staff': self.user.is_staff,
        }
        return data


class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [permissions.AllowAny]


class RegisterView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]


class MeView(generics.RetrieveAPIView):
    serializer_class = UsuarioMeSerializer

    def get_object(self):
        return self.request.user


class PerfilListView(generics.ListAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    permission_classes = [permissions.AllowAny]
