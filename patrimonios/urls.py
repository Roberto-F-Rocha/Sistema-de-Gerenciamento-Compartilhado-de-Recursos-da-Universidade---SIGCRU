from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatrimonioViewSet

router = DefaultRouter()
router.register(r'patrimonios', PatrimonioViewSet, basename='patrimonio')

urlpatterns = [
    path('', include(router.urls)),
    path('', include("patrimonios.api.urls_localizacao")),
]
