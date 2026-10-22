from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario, Perfil


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    search_fields = ('descricao',)


@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):
    list_display = ('email', 'nome', 'perfil', 'is_staff', 'is_active')
    list_filter = ('perfil', 'is_staff', 'is_active')
    search_fields = ('email', 'nome')
    ordering = ('nome',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Dados pessoais', {'fields': ('nome', 'data_nascimento', 'perfil')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'data_nascimento', 'perfil', 'password1', 'password2'),
        }),
    )
