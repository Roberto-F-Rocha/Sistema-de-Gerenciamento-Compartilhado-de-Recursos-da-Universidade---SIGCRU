from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManutencaoViewSet

router = DefaultRouter()
router.register(r'manutencoes', ManutencaoViewSet, basename='manutencao')

urlpatterns = [
    path('', include(router.urls)),
]
