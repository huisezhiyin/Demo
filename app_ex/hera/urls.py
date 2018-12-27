from rest_framework.routers import DefaultRouter
from app_ex.hera import views

router = DefaultRouter()
router.register(r'user', views.UserViewSet, base_name="user")
urlpatterns = router.urls
