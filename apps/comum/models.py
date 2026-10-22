from django.conf import settings
from django.db import models


class Administrador(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='administrador',
    )

    class Meta:
        verbose_name = 'administrador'
        verbose_name_plural = 'administradores'

    def __str__(self):
        return self.usuario.nome


class Categoria(models.Model):
    descricao = models.CharField('descrição', max_length=100, unique=True)

    class Meta:
        ordering = ['descricao']
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.descricao
