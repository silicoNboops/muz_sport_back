from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from muzsport.models import *
from muzsport.serializers import *
from django_filters.rest_framework import DjangoFilterBackend


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

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sports_name', 'tag_name', 'mood_name', 'country_name', 'with_words']


@csrf_exempt
def coupon_api(request):
    if request.method == 'GET':
        coupon_name = request.get('coupon_name')
        c = Coupons.objects.filter(coupon_name=coupon_name).first()

        print(c)

        if c:
            return c
        else:
            return None

