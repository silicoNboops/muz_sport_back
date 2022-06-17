from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from muzsport import views
from muzsport.views import *

urlpatterns = [
    path('tracks/', TrackReadOnlyModelViewSet.as_view({'get': 'list'})),
    path('tracks/<int:pk>/', TrackReadOnlyModelViewSet.as_view({'get': 'retrieve'})),
    path('tracks/filtersAll', views.track_fields_values),
    path('tracks/filter', views.track_filtered),
    path('sports/', SportsReadOnlyModelViewSet.as_view({'get': 'list'})),
    path('sports/<int:pk>/', SportsReadOnlyModelViewSet.as_view({'get': 'retrieve'})),
    path('tags/', TagsReadOnlyModelViewSet.as_view({'get': 'list'})),
    path('tags/<int:pk>/', TagsReadOnlyModelViewSet.as_view({'get': 'retrieve'})),
    path('moods/', MoodsReadOnlyModelViewSet.as_view({'get': 'list'})),
    path('moods/<int:pk>/', MoodsReadOnlyModelViewSet.as_view({'get': 'retrieve'})),
    path('country/', CountryReadOnlyModelViewSet.as_view({'get': 'list'})),
    path('country/<int:pk>/', CountryReadOnlyModelViewSet.as_view({'get': 'retrieve'})),
    path('order/', OrderViewSet.as_view({'get': 'list'})),
    path('order/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve'})),
    path('coupon/<str:coupon_name>', CouponsViewSet.as_view({'get': 'retrieve'})),
    path('order/create/', OrderViewSet.as_view({'post': 'create'})),
    path('order/segment/delete/', OrderSegmentDeleteViewSet.as_view({'post': 'create'})),
    path('order/segment/add/', OrderSegmentAddViewSet.as_view({'post': 'create'})),
    path('wishlist/', WishlistModelViewSet.as_view({'get': 'list'})),
    path('wishlist/<int:pk>/', WishlistModelViewSet.as_view({'get': 'retrieve'})),
    path('wishlist/create/', WishlistModelViewSet.as_view({'post': 'create'})),
    path('wishlist/delete/', WishlistModelViewSet.as_view({'delete': 'destroy'})),
    path('adbig/', AdBigPhotoFileViewSet.as_view({'get': 'list'})),
    path('adsmall/', AdSmallPhotoFileViewSet.as_view({'get': 'list'})),
    # path('subscription/', SubscriptionAPIView.as_view()),
    # path('subscription/<int:pk>', SubscriptionAPIDetailView.as_view()),

]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)