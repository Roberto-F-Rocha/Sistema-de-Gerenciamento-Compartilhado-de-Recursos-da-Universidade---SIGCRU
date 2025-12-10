from django.urls import path, include
from rest_framework.routers import DefaultRouter
from historico.views import HistoricoViewSet

router = DefaultRouter()
router.register(r"historico", HistoricoViewSet, basename="historico")

urlpatterns = [
    path("", include(router.urls)),
]