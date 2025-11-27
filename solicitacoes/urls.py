from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SolicitacaoViewSet, MinhasSolicitacoesView

router = DefaultRouter()
router.register(r"", SolicitacaoViewSet, basename="solicitacoes")

urlpatterns = [
    path("minhas/", MinhasSolicitacoesView.as_view(), name="minhas-solicitacoes"),
    path("", include(router.urls)),
]
