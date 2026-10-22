from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ConteudoSaudeMentalViewSet, FAQSaudeMentalViewSet,
    CanalApoioSaudeMentalViewSet, RelatoAnonimoSaudeMentalViewSet,
)

router = DefaultRouter()
router.register('conteudos', ConteudoSaudeMentalViewSet)
router.register('faqs', FAQSaudeMentalViewSet)
router.register('canais-apoio', CanalApoioSaudeMentalViewSet)
router.register('relatos', RelatoAnonimoSaudeMentalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
