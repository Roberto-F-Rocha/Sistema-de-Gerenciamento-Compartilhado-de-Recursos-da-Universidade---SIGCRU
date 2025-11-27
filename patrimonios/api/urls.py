from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EspacoFisicoViewSet

router = DefaultRouter()
router.register(r'espacos-fisicos', EspacoFisicoViewSet, basename='espaco-fisico')

urlpatterns = [
    path('', include(router.urls)),
]
