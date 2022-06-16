from functools import reduce

from django.db.models import Q, ForeignKey
from django.forms import BooleanField, JSONField, CharField
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.exceptions import NotFound, AuthenticationFailed
from rest_framework.filters import SearchFilter
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from muzsport.serializers import *
from muzsport.service import TracksFilter, TracksPagination


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
    filterset_class = TracksFilter
    pagination_class = TracksPagination

    def get_queryset(self):
        # radius = self.request.query_params.get('radius')

        pk = self.kwargs.get('pk')

        if not pk:
            filter_kwargs = []

            for item in self.request.query_params.items():
                # TODO продумать как для related полей делать проверку чтоб добавлять title к ним
                if not item[0] == 'page':
                    if item[0] == 'type':
                        filter_kwargs.append(Q(**{f'{item[0]}__title': item[1]}))
                    else:
                        filter_kwargs.append(Q(**{item[0]: item[1]}))

            # TODO выводим все (не только опубликованные)
            # filter_kwargs.append(Q(**{'is_published': True}))

            if filter_kwargs:
                products = Track.objects.filter(reduce(lambda a, b: a & b, filter_kwargs))
            else:
                products = Track.objects.all()

            return products

        # queryset должен возвращать список, а фильтр тоже всегда возвращает список
        return Track.objects.filter(pk=pk)

    def get_serializer_class(self):
        if self.action == 'list':
            return TrackSerializers


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


def get_filters_values(model_class, fields, excluded_fields):

    select_list = []
    checkbox_list = []

    for field in fields:
        field_name = field.name

        if field_name not in excluded_fields:
            if isinstance(field, BooleanField):
                checkbox_list.append(field.name)
            else:
                excludes = None

                if isinstance(field, JSONField):
                    # TODO не доделал
                    empty_q = Q(**{f'{field_name}__exact': '[]'})
                    excludes = (excludes and (excludes | empty_q)) or empty_q
                    # TODO на фронте делать мультиселект для таких полей
                else:
                    excludes = None

                    null_q = Q(**{f'{field_name}__isnull': True})
                    excludes = (excludes and (excludes | null_q)) or null_q
                    if isinstance(field, CharField):
                        empty_q = Q(**{f'{field_name}__exact': ''})
                        excludes = (excludes and (excludes | empty_q)) or empty_q

                    pre_excluded_values = model_class.objects.order_by(field_name).values_list(field_name, flat=True) \
                        .distinct()
                    values_minus_excluded = pre_excluded_values.exclude(excludes)
                    values = list(values_minus_excluded)

                    if values:
                        select = {'product_prop': field.name,
                                  'name': field.verbose_name,
                                  'values': values}

                        select_list.append(select)

    filter_variant_list = {
        'select': select_list,
        'checkbox': checkbox_list
    }
    return filter_variant_list


def get_filtered_query_set(model_class, req_query_params):
    filter_kwargs = []

    for item in req_query_params:
        # TODO продумать как для related полей делать проверку чтоб добавлять title к ним
        if item[0] == 'type':
            filter_kwargs.append(Q(**{f'{item[0]}__title': item[1]}))
        else:
            filter_kwargs.append(Q(**{item[0]: item[1]}))

    if filter_kwargs:
        filtered_query_set = model_class.objects.filter(reduce(lambda a, b: a & b, filter_kwargs))
    else:
        filtered_query_set = model_class.objects.all()

    return filtered_query_set


def track_fields_values(request):
    if request.method == 'GET':
        fields = [f for f in Track._meta.fields]
        excluded_fields = ['file', 'photo', 'author', 'title', 'price', 'tag_name']

        fields_variant_list = get_filters_values(Track, fields, excluded_fields)

        return JsonResponse(fields_variant_list, safe=False)


def track_filtered(request):
    if request.method == 'GET':
        query_set = get_filtered_query_set(Track, request.GET.items())

        serializer = TrackSerializers(query_set, many=True)

        return JsonResponse(serializer.data, safe=False)


def subscription_email(request):
    if request.method == 'POST':
        email_data = JSONParser().parse(request)
        email_serializer = EmailSerializers(data=email_data)

        if email_serializer.is_valid():
            email_serializer.save()

    elif request.method == 'GET':
        subscription = MyUser.objects.all()
        email_serializer = EmailSerializers(subscription, many=True)

        return JsonResponse(email_serializer.data, safe=False)
