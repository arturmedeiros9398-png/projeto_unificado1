from django.conf import settings
from django.db import models
from django.utils import timezone

from apps.comum.models import Administrador, Categoria


class ConteudoSaudeMental(models.Model):
    STATUS_CHOICES = [
        ('publicado', 'Publicado'),
        ('rascunho', 'Rascunho'),
    ]

    titulo = models.CharField(max_length=200)
    resumo = models.TextField(blank=True, default='')
    texto = models.TextField(blank=True, default='')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='publicado')
    autor = models.CharField(max_length=150, blank=True)
    autor_usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='conteudos_saude_mental',
    )
    fonte = models.CharField(max_length=200, blank=True)
    url = models.URLField(blank=True)
    data_publicacao = models.DateField(default=timezone.localdate)
    administrador = models.ForeignKey(
        Administrador,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='conteudos_saude_mental',
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='conteudos_saude_mental',
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-data_publicacao', 'titulo']
        verbose_name = 'conteúdo (saúde mental)'
        verbose_name_plural = 'conteúdos (saúde mental)'

    def __str__(self):
        return self.titulo


class FAQSaudeMental(models.Model):
    pergunta = models.CharField(max_length=300)
    resposta = models.TextField()
    administrador = models.ForeignKey(
        Administrador,
        on_delete=models.PROTECT,
        related_name='faqs_saude_mental',
        null=True,
        blank=True,
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pergunta']
        verbose_name = 'FAQ (saúde mental)'
        verbose_name_plural = 'FAQs (saúde mental)'

    def __str__(self):
        return self.pergunta


class CanalApoioSaudeMental(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=30, blank=True)
    endereco = models.CharField('endereço', max_length=255, blank=True)
    administrador = models.ForeignKey(
        Administrador,
        on_delete=models.PROTECT,
        related_name='canais_apoio_saude_mental',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['nome']
        verbose_name = 'canal de apoio (saúde mental)'
        verbose_name_plural = 'canais de apoio (saúde mental)'

    def __str__(self):
        return self.nome


class RelatoAnonimoSaudeMental(models.Model):
    mensagem = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_publicacao']
        verbose_name = 'relato anônimo (saúde mental)'
        verbose_name_plural = 'relatos anônimos (saúde mental)'

    def __str__(self):
        return f'Relato #{self.pk}'
