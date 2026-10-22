from django.contrib import admin
from .models import (
    ConteudoSaudeMental, FAQSaudeMental,
    CanalApoioSaudeMental, RelatoAnonimoSaudeMental,
)


@admin.register(ConteudoSaudeMental)
class ConteudoSaudeMentalAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'categoria', 'data_publicacao')
    list_filter = ('status', 'categoria')
    search_fields = ('titulo', 'resumo')


@admin.register(FAQSaudeMental)
class FAQSaudeMentalAdmin(admin.ModelAdmin):
    list_display = ('pergunta',)


@admin.register(CanalApoioSaudeMental)
class CanalApoioSaudeMentalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')


@admin.register(RelatoAnonimoSaudeMental)
class RelatoAnonimoSaudeMentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_publicacao')
    readonly_fields = ('mensagem', 'data_publicacao')
