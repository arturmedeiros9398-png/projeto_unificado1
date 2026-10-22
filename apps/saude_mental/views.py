from rest_framework import viewsets, permissions

from .models import (
    ConteudoSaudeMental, FAQSaudeMental,
    CanalApoioSaudeMental, RelatoAnonimoSaudeMental,
)
from .serializers import (
    ConteudoSaudeMentalSerializer, FAQSaudeMentalSerializer,
    CanalApoioSaudeMentalSerializer, RelatoAnonimoSaudeMentalSerializer,
)
from apps.users.permissions import IsAdmin, IsProfessorOrAdmin


class ConteudoSaudeMentalViewSet(viewsets.ModelViewSet):
    queryset = ConteudoSaudeMental.objects.select_related(
        'categoria', 'autor_usuario', 'administrador'
    )
    serializer_class = ConteudoSaudeMentalSerializer

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


class FAQSaudeMentalViewSet(viewsets.ModelViewSet):
    queryset = FAQSaudeMental.objects.all()
    serializer_class = FAQSaudeMentalSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [permissions.AllowAny()]
        return [IsAdmin()]


class CanalApoioSaudeMentalViewSet(viewsets.ModelViewSet):
    queryset = CanalApoioSaudeMental.objects.all()
    serializer_class = CanalApoioSaudeMentalSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [permissions.AllowAny()]
        return [IsAdmin()]


class RelatoAnonimoSaudeMentalViewSet(viewsets.ModelViewSet):
    queryset = RelatoAnonimoSaudeMental.objects.all()
    serializer_class = RelatoAnonimoSaudeMentalSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [IsAdmin()]
