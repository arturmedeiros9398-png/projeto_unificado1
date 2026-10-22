from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from apps.comum.models import Administrador, Categoria


class ConteudoDrogas(models.Model):
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
        related_name='conteudos_drogas',
    )
    fonte = models.CharField(max_length=200, blank=True)
    url = models.URLField(blank=True)
    data_publicacao = models.DateField(default=timezone.localdate)
    administrador = models.ForeignKey(
        Administrador,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='conteudos_drogas',
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='conteudos_drogas',
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-data_publicacao', 'titulo']
        verbose_name = 'conteúdo (drogas)'
        verbose_name_plural = 'conteúdos (drogas)'

    def __str__(self):
        return self.titulo

    @property
    def media_avaliacao(self):
        res = self.avaliacoes.aggregate(models.Avg('nota'))['nota__avg']
        return round(res, 1) if res is not None else None

    @property
    def total_avaliacoes(self):
        return self.avaliacoes.count()


class AvaliacaoConteudoDrogas(models.Model):
    conteudo = models.ForeignKey(
        ConteudoDrogas,
        on_delete=models.CASCADE,
        related_name='avaliacoes',
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='avaliacoes_drogas',
    )
    nota = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    comentario = models.TextField(blank=True, default='')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['conteudo', 'usuario'],
                name='unique_avaliacao_drogas_por_usuario',
            )
        ]
        ordering = ['-atualizado_em']
        verbose_name = 'avaliação de conteúdo (drogas)'
        verbose_name_plural = 'avaliações de conteúdo (drogas)'

    def __str__(self):
        return f'{self.usuario.nome} → {self.conteudo.titulo}: {self.nota}★'


class FAQDrogas(models.Model):
    pergunta = models.CharField(max_length=300)
    resposta = models.TextField()
    administrador = models.ForeignKey(
        Administrador,
        on_delete=models.PROTECT,
        related_name='faqs_drogas',
        null=True,
        blank=True,
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pergunta']
        verbose_name = 'FAQ (drogas)'
        verbose_name_plural = 'FAQs (drogas)'

    def __str__(self):
        return self.pergunta


class CanalApoioDrogas(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=30, blank=True)
    endereco = models.CharField('endereço', max_length=255, blank=True)
    administrador = models.ForeignKey(
        Administrador,
        on_delete=models.PROTECT,
        related_name='canais_apoio_drogas',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['nome']
        verbose_name = 'canal de apoio (drogas)'
        verbose_name_plural = 'canais de apoio (drogas)'

    def __str__(self):
        return self.nome


class RelatoAnonimoDrogas(models.Model):
    mensagem = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_publicacao']
        verbose_name = 'relato anônimo (drogas)'
        verbose_name_plural = 'relatos anônimos (drogas)'

    def __str__(self):
        return f'Relato #{self.pk}'
