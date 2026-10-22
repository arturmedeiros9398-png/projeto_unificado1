from django.contrib import admin
from .models import Administrador, Categoria


@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario')
    search_fields = ('usuario__nome', 'usuario__email')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    search_fields = ('descricao',)
