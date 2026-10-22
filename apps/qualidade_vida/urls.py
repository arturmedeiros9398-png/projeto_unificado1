from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ConteudoQualidadeVidaViewSet, FAQQualidadeVidaViewSet,
    CanalApoioQualidadeVidaViewSet, RelatoAnonimoQualidadeVidaViewSet,
)

router = DefaultRouter()
router.register('conteudos', ConteudoQualidadeVidaViewSet)
router.register('faqs', FAQQualidadeVidaViewSet)
router.register('canais-apoio', CanalApoioQualidadeVidaViewSet)
router.register('relatos', RelatoAnonimoQualidadeVidaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
