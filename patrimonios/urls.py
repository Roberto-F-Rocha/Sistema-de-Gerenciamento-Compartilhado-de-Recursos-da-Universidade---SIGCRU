from rest_framework.routers import DefaultRouter
from .views import PatrimonioViewSet

router = DefaultRouter()
router.register(r'patrimonios', PatrimonioViewSet, basename='patrimonio')

urlpatterns = router.urls
