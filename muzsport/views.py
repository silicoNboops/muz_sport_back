from rest_framework import generics
from django.shortcuts import render
from muzsport.models import Track, User, Coupons, Order
from muzsport.serializers import (
    TrackSerializers,
    UserSerializers,
    CouponsSerializers,
    OrderSerializers
)


class TrackAPIView(generics.ListAPIView):
    queryset = Track.objects.all()