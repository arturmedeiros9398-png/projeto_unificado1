from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Administrador, Categoria
from .serializers import AdministradorSerializer, CategoriaSerializer
from apps.users.permissions import IsAdmin


class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.select_related('usuario').all()
    serializer_class = AdministradorSerializer
    permission_classes = [IsAdmin]


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
