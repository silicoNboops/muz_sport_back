from rest_framework import serializers
from muzsport.models import Track, Account, Coupons, Order


class TrackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('author', 'title', 'sport_name', 'price', 'beginning_peak', 'sportsman_name', 'photo', 'track_length')


class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('mobile_number', 'coupons')


class CouponsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coupons
        fields = ('validity_period', )


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_number', 'order_date', 'price')
