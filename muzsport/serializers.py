from rest_framework import serializers
from muzsport.models import Track, Coupons, Order


class TrackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'


class CouponsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coupons
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
