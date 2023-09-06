from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'blogs', views.BlogPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # ... (Bạn có thể thêm các URLs khác nếu bạn có thêm views)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)