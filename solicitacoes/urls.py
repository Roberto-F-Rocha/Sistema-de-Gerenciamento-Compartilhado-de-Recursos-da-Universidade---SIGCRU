from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SolicitacaoViewSet

router = DefaultRouter()
router.register(r"", SolicitacaoViewSet, basename="solicitacoes")

urlpatterns = [
    path("", include(router.urls)),
]
