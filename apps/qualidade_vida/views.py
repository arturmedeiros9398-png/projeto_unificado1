from rest_framework import viewsets, permissions

from .models import (
    ConteudoQualidadeVida, FAQQualidadeVida,
    CanalApoioQualidadeVida, RelatoAnonimoQualidadeVida,
)
from .serializers import (
    ConteudoQualidadeVidaSerializer, FAQQualidadeVidaSerializer,
    CanalApoioQualidadeVidaSerializer, RelatoAnonimoQualidadeVidaSerializer,
)
from apps.users.permissions import IsAdmin, IsProfessorOrAdmin


class ConteudoQualidadeVidaViewSet(viewsets.ModelViewSet):
    queryset = ConteudoQualidadeVida.objects.select_related(
        'categoria', 'autor_usuario', 'administrador'
    )
    serializer_class = ConteudoQualidadeVidaSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [permissions.AllowAny()]
        return [IsProfessorOrAdmin()]

    def get_queryset(self):
        qs = super().get_queryset()
        if self.action in ('list', 'retrieve') and not (
            self.request.user.is_authenticated and (
                self.request.user.is_staff or
                getattr(self.request.user, 'perfil', None) and
                self.request.user.perfil.descricao in ('Administrador', 'Professor')
            )
        ):
            qs = qs.filter(status='publicado')
        return qs


class FAQQualidadeVidaViewSet(viewsets.ModelViewSet):
    queryset = FAQQualidadeVida.objects.all()
    serializer_class = FAQQualidadeVidaSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [permissions.AllowAny()]
        return [IsAdmin()]


class CanalApoioQualidadeVidaViewSet(viewsets.ModelViewSet):
    queryset = CanalApoioQualidadeVida.objects.all()
    serializer_class = CanalApoioQualidadeVidaSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [permissions.AllowAny()]
        return [IsAdmin()]


class RelatoAnonimoQualidadeVidaViewSet(viewsets.ModelViewSet):
    queryset = RelatoAnonimoQualidadeVida.objects.all()
    serializer_class = RelatoAnonimoQualidadeVidaSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [IsAdmin()]
