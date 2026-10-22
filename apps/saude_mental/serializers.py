from rest_framework import serializers
from .models import (
    ConteudoSaudeMental, FAQSaudeMental,
    CanalApoioSaudeMental, RelatoAnonimoSaudeMental,
)


class ConteudoSaudeMentalSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(source='categoria.descricao', read_only=True)
    autor_usuario_nome = serializers.CharField(source='autor_usuario.nome', read_only=True)

    class Meta:
        model = ConteudoSaudeMental
        fields = (
            'id', 'titulo', 'resumo', 'texto', 'status',
            'autor', 'autor_usuario', 'autor_usuario_nome',
            'fonte', 'url', 'data_publicacao',
            'administrador', 'categoria', 'categoria_nome',
            'criado_em', 'atualizado_em',
        )
        read_only_fields = ('criado_em', 'atualizado_em')


class FAQSaudeMentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQSaudeMental
        fields = ('id', 'pergunta', 'resposta', 'administrador', 'criado_em')
        read_only_fields = ('criado_em',)


class CanalApoioSaudeMentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanalApoioSaudeMental
        fields = ('id', 'nome', 'telefone', 'endereco', 'administrador')


class RelatoAnonimoSaudeMentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatoAnonimoSaudeMental
        fields = ('id', 'mensagem', 'data_publicacao')
        read_only_fields = ('data_publicacao',)
