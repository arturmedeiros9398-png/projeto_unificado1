from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ConteudoDrogasViewSet, FAQDrogasViewSet,
    CanalApoioDrogasViewSet, RelatoAnonimoDrogasViewSet,
)

router = DefaultRouter()
router.register('conteudos', ConteudoDrogasViewSet)
router.register('faqs', FAQDrogasViewSet)
router.register('canais-apoio', CanalApoioDrogasViewSet)
router.register('relatos', RelatoAnonimoDrogasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
