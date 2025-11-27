from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EspacoFisicoViewSet, LocalizacaoViewSet

router = DefaultRouter()
router.register(r'espacos-fisicos', EspacoFisicoViewSet, basename='espaco-fisico')
router.register(r'localizacoes', LocalizacaoViewSet, basename='localizacao')

urlpatterns = [
    path('', include(router.urls)),
]
