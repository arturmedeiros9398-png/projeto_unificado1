from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    ConteudoDrogas, AvaliacaoConteudoDrogas,
    FAQDrogas, CanalApoioDrogas, RelatoAnonimoDrogas,
)
from .serializers import (
    ConteudoDrogasSerializer, AvaliacaoConteudoDrogasSerializer,
    FAQDrogasSerializer, CanalApoioDrogasSerializer, RelatoAnonimoDrogasSerializer,
)
from apps.users.permissions import IsAdmin, IsProfessorOrAdmin


class ConteudoDrogasViewSet(viewsets.ModelViewSet):
    queryset = ConteudoDrogas.objects.select_related(
        'categoria', 'autor_usuario', 'administrador'
    ).prefetch_related('avaliacoes')
    serializer_class = ConteudoDrogasSerializer

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

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def avaliar(self, request, pk=None):
        conteudo = self.get_object()
        serializer = AvaliacaoConteudoDrogasSerializer(data={
            **request.data,
            'conteudo': conteudo.pk,
        })
        serializer.is_valid(raise_exception=True)
        AvaliacaoConteudoDrogas.objects.update_or_create(
            conteudo=conteudo,
            usuario=request.user,
            defaults={
                'nota': serializer.validated_data['nota'],
                'comentario': serializer.validated_data.get('comentario', ''),
            },
        )
        return Response(ConteudoDrogasSerializer(conteudo, context={'request': request}).data)


class FAQDrogasViewSet(viewsets.ModelViewSet):
    queryset = FAQDrogas.objects.all()
    serializer_class = FAQDrogasSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [permissions.AllowAny()]
        return [IsAdmin()]


class CanalApoioDrogasViewSet(viewsets.ModelViewSet):
    queryset = CanalApoioDrogas.objects.all()
    serializer_class = CanalApoioDrogasSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [permissions.AllowAny()]
        return [IsAdmin()]


class RelatoAnonimoDrogasViewSet(viewsets.ModelViewSet):
    queryset = RelatoAnonimoDrogas.objects.all()
    serializer_class = RelatoAnonimoDrogasSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]  # relato anônimo
        if self.action in ('list', 'retrieve'):
            return [IsAdmin()]
        return [IsAdmin()]
