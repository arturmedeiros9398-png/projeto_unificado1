from rest_framework import serializers
from .models import Administrador, Categoria


class AdministradorSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.CharField(source='usuario.nome', read_only=True)
    usuario_email = serializers.CharField(source='usuario.email', read_only=True)

    class Meta:
        model = Administrador
        fields = ('id', 'usuario', 'usuario_nome', 'usuario_email')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'descricao')
