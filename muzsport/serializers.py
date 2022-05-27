from rest_framework import serializers
from muzsport.models import *


class SportsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class TagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class MoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


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


# class ProductListSerializers(serializers.ModelSerializer):
#     model = Track, Sports, Moods, Tags, Order
#     fields = '__all__'



