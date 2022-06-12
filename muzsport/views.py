from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.exceptions import NotFound, AuthenticationFailed
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from muzsport.serializers import *


class SportsReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrackSerializers
    queryset = Track.objects.all()


class TagsReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrackSerializers
    queryset = Track.objects.all()


class MoodsReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrackSerializers
    queryset = Track.objects.all()


class CountryReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrackSerializers
    queryset = Track.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()


class TrackReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrackSerializers
    queryset = Track.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['sports_name', 'tag_name', 'mood_name', 'with_words', 'country_name']
    search_fields = ['author', 'title']


class CouponsViewSet(viewsets.ModelViewSet):
    serializer_class = CouponsSerializers
    queryset = Coupons.objects.all()
    lookup_field = 'coupon_name'


class OrderSegmentDeleteViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSegmentDeleteSerializers
    queryset = OrderSegmentDelete.objects.all()


class OrderSegmentAddViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSegmentAddSerializers
    queryset = OrderSegmentAdd.objects.all()


class AdBigPhotoFileViewSet(viewsets.ModelViewSet):
    serializer_class = AdBigPhotoFileSerializers
    queryset = AdBigPhotoFile.objects.all()


class AdSmallPhotoFileViewSet(viewsets.ModelViewSet):
    serializer_class = AdSmallPhotoFileSerializers
    queryset = AdSmallPhotoFile.objects.all()


class WishlistModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            wished_track = Track.objects.get(id=self.kwargs['pk'])
            return serializer.save(user=self.request.user, wished_track=wished_track)
        except:
            raise NotFound

    def get_queryset(self):
        if self.action == 'list' or self.action == 'retrieve':
            return Wishlist.objects.filter(user_id=self.request.user.id)
        elif self.action == 'post' or self.action == 'destroy':
            return Wishlist.objects.filter(user_id=self.request.user.id)

    def get_serializer_class(self):
        try:
            if self.action == 'list':
                return WishlistSerializers
            if self.action == 'retrieve':
                return WishlistSerializers
            if self.action == 'create':
                return WishlistCreateSerializers
            elif self.action == 'destroy':
                return WishlistDeleteSerializers
        except:
            raise AuthenticationFailed
