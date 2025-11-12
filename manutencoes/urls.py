from rest_framework.routers import DefaultRouter
from .views import ManutencaoViewSet

router = DefaultRouter()
router.register(r'manutencoes', ManutencaoViewSet, basename='manutencao')

urlpatterns = router.urls
