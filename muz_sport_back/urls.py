from django.contrib import admin
from django.urls import path, include

from muzsport.views import OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')
urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('auth/', include("djoser.urls.jwt")),
    path('auth/', include("djoser.urls")),
    path('auth/', include("djoser.urls.authtoken")),
]