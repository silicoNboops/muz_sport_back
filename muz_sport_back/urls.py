from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from muzsport import views
from muzsport.views import CouponsViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="CodifyHR API",
      default_version='v1',
      description="special for frontend ^^",
      contact=openapi.Contact(email="maxlestor2@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("rest_framework.urls")),
    path('auth/', include("djoser.urls.jwt")),
    path('auth/', include("djoser.urls")),
    path('auth/', include("djoser.urls.authtoken")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include('muzsport.urls')),
]