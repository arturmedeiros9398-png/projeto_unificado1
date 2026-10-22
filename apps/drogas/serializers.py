from rest_framework import serializers
from .models import (
    ConteudoDrogas, AvaliacaoConteudoDrogas,
    FAQDrogas, CanalApoioDrogas, RelatoAnonimoDrogas,
)


class AvaliacaoConteudoDrogasSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.CharField(source='usuario.nome', read_only=True)

    class Meta:
        model = AvaliacaoConteudoDrogas
        fields = (
            'id', 'conteudo', 'usuario', 'usuario_nome',
            'nota', 'comentario', 'criado_em', 'atualizado_em',
        )
        read_only_fields = ('id', 'usuario', 'usuario_nome', 'criado_em', 'atualizado_em')


class ConteudoDrogasSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(source='categoria.descricao', read_only=True)
    autor_usuario_nome = serializers.CharField(source='autor_usuario.nome', read_only=True)
    media_avaliacao = serializers.FloatField(read_only=True)
    total_avaliacoes = serializers.IntegerField(read_only=True)
    minha_avaliacao = serializers.SerializerMethodField()

    class Meta:
        model = ConteudoDrogas
        fields = (
            'id', 'titulo', 'resumo', 'texto', 'status',
            'autor', 'autor_usuario', 'autor_usuario_nome',
            'fonte', 'url', 'data_publicacao',
            'administrador', 'categoria', 'categoria_nome',
            'media_avaliacao', 'total_avaliacoes', 'minha_avaliacao',
            'criado_em', 'atualizado_em',
        )
        read_only_fields = ('criado_em', 'atualizado_em')

    def get_minha_avaliacao(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return None
        av = obj.avaliacoes.filter(usuario=request.user).first()
        if av:
            return {'id': av.id, 'nota': av.nota, 'comentario': av.comentario}
        return None


class FAQDrogasSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQDrogas
        fields = ('id', 'pergunta', 'resposta', 'administrador', 'criado_em')
        read_only_fields = ('criado_em',)


class CanalApoioDrogasSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanalApoioDrogas
        fields = ('id', 'nome', 'telefone', 'endereco', 'administrador')


class RelatoAnonimoDrogasSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatoAnonimoDrogas
        fields = ('id', 'mensagem', 'data_publicacao')
        read_only_fields = ('data_publicacao',)
