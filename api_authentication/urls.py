from .views import CustomUserViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    # Các URL patterns khác của ứng dụng của bạn
    path('', include(router.urls)),
]