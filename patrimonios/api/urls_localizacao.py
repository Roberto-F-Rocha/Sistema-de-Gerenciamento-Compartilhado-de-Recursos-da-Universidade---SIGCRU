from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_localizacao import LocalizacaoViewSet

router = DefaultRouter()
router.register("localizacoes", LocalizacaoViewSet, basename="localizacao")

urlpatterns = [
    path("", include(router.urls)),
]
