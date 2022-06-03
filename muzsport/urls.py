from django.urls import path

from muzsport import views
from muzsport.views import *

urlpatterns = [
    path('tracks/', TrackReadOnlyModelViewSet.as_view({'get': 'list'})),
    path('tracks/<int:pk>/', TrackReadOnlyModelViewSet.as_view({'get': 'retrieve'})),
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
]