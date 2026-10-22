from django.contrib import admin
from .models import (
    ConteudoQualidadeVida, FAQQualidadeVida,
    CanalApoioQualidadeVida, RelatoAnonimoQualidadeVida,
)


@admin.register(ConteudoQualidadeVida)
class ConteudoQualidadeVidaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'categoria', 'data_publicacao')
    list_filter = ('status', 'categoria')
    search_fields = ('titulo', 'resumo')


@admin.register(FAQQualidadeVida)
class FAQQualidadeVidaAdmin(admin.ModelAdmin):
    list_display = ('pergunta',)


@admin.register(CanalApoioQualidadeVida)
class CanalApoioQualidadeVidaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')


@admin.register(RelatoAnonimoQualidadeVida)
class RelatoAnonimoQualidadeVidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_publicacao')
    readonly_fields = ('mensagem', 'data_publicacao')
