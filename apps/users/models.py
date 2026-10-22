from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class Perfil(models.Model):
    descricao = models.CharField('descrição', max_length=80, unique=True)

    class Meta:
        ordering = ['descricao']
        verbose_name = 'perfil'
        verbose_name_plural = 'perfis'

    def __str__(self):
        return self.descricao


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff') or not extra_fields.get('is_superuser'):
            raise ValueError('Superusuários devem ter is_staff=True e is_superuser=True.')

        perfil, _ = Perfil.objects.get_or_create(descricao='Administrador')
        extra_fields.setdefault('perfil', perfil)
        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    """Usuário centralizado. Login via e-mail."""

    email = models.EmailField(primary_key=True, max_length=150)
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.PROTECT,
        related_name='usuarios',
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'data_nascimento']

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome} ({self.email})'
