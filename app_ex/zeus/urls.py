from rest_framework.routers import DefaultRouter
from app_ex.zeus import views

router = DefaultRouter()
router.register(r'hello', views.HelloWorldViewSet, base_name="hello")
urlpatterns = router.urls
