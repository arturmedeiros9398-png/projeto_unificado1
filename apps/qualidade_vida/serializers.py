from rest_framework import serializers
from .models import (
    ConteudoQualidadeVida, FAQQualidadeVida,
    CanalApoioQualidadeVida, RelatoAnonimoQualidadeVida,
)


class ConteudoQualidadeVidaSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(source='categoria.descricao', read_only=True)
    autor_usuario_nome = serializers.CharField(source='autor_usuario.nome', read_only=True)

    class Meta:
        model = ConteudoQualidadeVida
        fields = (
            'id', 'titulo', 'resumo', 'texto', 'status',
            'autor', 'autor_usuario', 'autor_usuario_nome',
            'fonte', 'url', 'data_publicacao',
            'administrador', 'categoria', 'categoria_nome',
            'criado_em', 'atualizado_em',
        )
        read_only_fields = ('criado_em', 'atualizado_em')


class FAQQualidadeVidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQQualidadeVida
        fields = ('id', 'pergunta', 'resposta', 'administrador', 'criado_em')
        read_only_fields = ('criado_em',)


class CanalApoioQualidadeVidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanalApoioQualidadeVida
        fields = ('id', 'nome', 'telefone', 'endereco', 'administrador')


class RelatoAnonimoQualidadeVidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatoAnonimoQualidadeVida
        fields = ('id', 'mensagem', 'data_publicacao')
        read_only_fields = ('data_publicacao',)
