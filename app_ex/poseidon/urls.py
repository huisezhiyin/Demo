from rest_framework.routers import DefaultRouter
from app_ex.poseidon import views

router = DefaultRouter()
router.register(r'commodity', views.CommodityViewSet, base_name="commodity")
urlpatterns = router.urls
