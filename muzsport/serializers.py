from rest_framework import serializers
from muzsport.models import *


class SportsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sports
        fields = '__all__'


class TagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class MoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Moods
        fields = '__all__'


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


# class ReturnSportsNameSerializer(serializers.RelatedField):
#     def to_representation(self, field_id):
#         return field_id.sports_name


class TrackSerializers(serializers.ModelSerializer):
    # sports_name = SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Track
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(TrackSerializers, self).to_representation(instance)
        rep['sports_name'] = instance.sports_name.sports_name
        rep['country_name'] = instance.country_name.country_name
        return rep


class CouponsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coupons
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderSegmentDeleteSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderSegmentDelete
        fields = '__all__'


class OrderSegmentAddSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderSegmentAdd
        fields = '__all__'


class AdBigPhotoFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdBigPhotoFile
        fields = '__all__'


class AdSmallPhotoFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdSmallPhotoFile
        fields = '__all__'


class WishlistSerializers(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only=True)
    wished_track = TrackSerializers()

    class Meta:
        model = Wishlist
        fields = '__all__'


class SuggestiveEffectSerializers(serializers.ModelSerializer):
    class Meta:
        model = SuggestiveEffect
        fields = '__all__'


class WishlistCreateSerializers(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only=True)
    wished_track = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Wishlist
        fields = '__all__'


class WishlistDeleteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'


class EmailSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'


# class ProductListSerializers(serializers.ModelSerializer):
#     model = Track, Sports, Moods, Tags, Order
#     fields = '__all__'



