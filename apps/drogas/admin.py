from django.contrib import admin
from .models import (
    ConteudoDrogas, AvaliacaoConteudoDrogas,
    FAQDrogas, CanalApoioDrogas, RelatoAnonimoDrogas,
)


@admin.register(ConteudoDrogas)
class ConteudoDrogasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'categoria', 'data_publicacao')
    list_filter = ('status', 'categoria')
    search_fields = ('titulo', 'resumo')


@admin.register(AvaliacaoConteudoDrogas)
class AvaliacaoConteudoDrogasAdmin(admin.ModelAdmin):
    list_display = ('conteudo', 'usuario', 'nota', 'atualizado_em')


@admin.register(FAQDrogas)
class FAQDrogasAdmin(admin.ModelAdmin):
    list_display = ('pergunta',)


@admin.register(CanalApoioDrogas)
class CanalApoioDrogasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')


@admin.register(RelatoAnonimoDrogas)
class RelatoAnonimoDrogasAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_publicacao')
    readonly_fields = ('mensagem', 'data_publicacao')
