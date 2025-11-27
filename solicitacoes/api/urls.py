from django.urls import path
from .views import MinhasSolicitacoesView

urlpatterns = [
    path("minhas/", MinhasSolicitacoesView.as_view(), name="minhas-solicitacoes"),
]