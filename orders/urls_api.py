from rest_framework.routers import DefaultRouter
from .views_api import CustomerViewSet, ProductViewSet, OrderViewSet

router = DefaultRouter()
router.register(r"customers", CustomerViewSet)
router.register(r"products", ProductViewSet)
router.register(r"orders", OrderViewSet)

urlpatterns = router.urls
