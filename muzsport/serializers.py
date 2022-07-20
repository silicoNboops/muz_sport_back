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


class DirectionMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectionMusic
        fields = '__all__'


class DirectionEffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectionEffect
        fields = '__all__'


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class PriceModificationAndServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = PriceModificationAndServices
        fields = '__all__'


# class ReturnSportsNameSerializer(serializers.RelatedField):
#     def to_representation(self, field_id):
#         return field_id.sports_name


class TrackSerializers(serializers.ModelSerializer):

    # direction_music = serializers.PrimaryKeyRelatedField(read_only=True)
    # mood_name = serializers.PrimaryKeyRelatedField(read_only=True)

    # TODO разобраться с длительностью трека
    class Meta:
        model = Track
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(TrackSerializers, self).to_representation(instance)
        rep['sports_name'] = instance.sports_name.sports_name
        rep['country_name'] = instance.country_name.country_name
        rep['direction_music'] = instance.direction_music.all().values_list('direction_music', flat=True)
        rep['mood_name'] = list(instance.mood_name.all().values_list('mood_name', flat=True))
        rep['variants'] = instance.variants.all().values().annotate(('direction_music'))
        return rep


class CouponsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coupons
        fields = '__all__'


class FooterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(FooterSerializers, self).to_representation(instance)
        rep['payment_icons'] = list(instance.payment_icons.all().values_list('icon', flat=True))
        return rep


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


class UnloadingModuleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UnloadingModule
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
        model = User
        fields = 'id', 'subscription', 'subscription_email'


class TrackModificationSerializer(serializers.ModelSerializer):
    # track = TrackSerializers()
    track = TrackSerializers
    sports_name = SportsSerializers
    suggestive_effect = SuggestiveEffectSerializers
    # order_segment_delete = serializers.ManyRelatedField()

    class Meta:
        model = TrackModification
        fields = '__all__'


class TrackModificationCreateSerializers(serializers.ModelSerializer):
    track = serializers.PrimaryKeyRelatedField(read_only=True)
    sports_name = serializers.PrimaryKeyRelatedField(read_only=True)
    suggestive_effect = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = TrackModification
        fields = '__all__'


class TrackModificationDeleteSerializers(serializers.ModelSerializer):
    class Meta:
        model = TrackModification
        fields = '__all__'


class CustomTrackSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomTrack
        fields = '__all__'


class AddTrackToTheProgramSerializers(serializers.ModelSerializer):
    class Meta:
        model = AddTrackToTheProgram
        fields = '__all__'

#
# class ProductListSerializers(serializers.ModelSerializer):
#     model = Track, Sports, Moods, Tags, Order
#     fields = '__all__'



