from functools import reduce

import django_filters
from django.db.models import Q, ForeignKey, ManyToManyField, F, BooleanField, CharField
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.exceptions import AuthenticationFailed, APIException, NotFound
from rest_framework.filters import SearchFilter
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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


class SportsAPIView(generics.ListCreateAPIView):
    serializer_class = SportsSerializers
    queryset = Sports.objects.all()


class PriceModificationAndServicesAPIView(generics.ListCreateAPIView):
    serializer_class = PriceModificationAndServicesSerializers
    queryset = PriceModificationAndServices.objects.all()


class PriceModificationAndServicesAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PriceModificationAndServicesSerializers
    queryset = PriceModificationAndServices.objects.all()


class DirectionEffectAPIView(generics.ListCreateAPIView):
    serializer_class = DirectionEffectSerializer
    queryset = DirectionEffect.objects.all()



class CountryReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrackSerializers
    queryset = Track.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    # def create(self, request, *args, **kwargs):
    #     order = Order.objects.create()
    #     order.save()
    #     super(OrderViewSet, self).create(order)

    def perform_create(self, serializer):
        try:
            print(f'GOV: {self.request.data}')

            try:
                # print('user:')
                customer = self.request.user
                print(customer)
            except User.DoesNotExist as e:
                print(type(e))
                customer = None

            try:
                # print('sport')
                sport = Sports.objects.get(id=self.request.data['sport'])
                print(sport)
            except Sports.DoesNotExist as e:
                print(type(e))
                sport = None

            suggestive_front = self.request.data.get('suggestiveEffect')
            if suggestive_front:
                try:
                    suggestive = SuggestiveEffect.objects.get(id=suggestive_front)
                    print(suggestive)
                except SuggestiveEffect.DoesNotExist as e:
                    suggestive = None
            else:
                suggestive = None

            track_front = self.request.data.get('track')
            if track_front:
                try:
                    track = Track.objects.get(id=track_front)
                    # TODO такого не может быть
                except Track.DoesNotExist as e:
                    print(type(e))
                    track = None
            else:
                track = None

            track_custom_front = self.request.data.get('trackCustom')
            if track_custom_front:
                try:
                    track_custom = CustomTrack.objects.get(id=self.request.data['trackCustom'])
                except SuggestiveEffect.DoesNotExist as e:
                    track_custom = None
            else:
                track_custom = None

            add_tracks = []
            additional_tracks_front = self.request.data.get('additionalTracks')
            if additional_tracks_front:
                for additional_track_id in additional_tracks_front:
                    try:
                        add_track_elem = AddTrackToTheProgram.objects.get(id=additional_track_id)
                        print(add_track_elem)
                        add_tracks.append(add_track_elem)
                    except AddTrackToTheProgram.DoesNotExist as e:
                        print(type(e))
                        add_track_elem = None

            return serializer.save(customer=customer, track=track, track_custom=track_custom,
                                   track_modification=None)
        except Exception as e:
            print(e)
            raise APIException

    def get_queryset(self):
        if self.action == 'list' or self.action == 'retrieve':
            return Order.objects.filter(customer_id=self.request.user.id)
        # if self.action == 'list' or self.action == 'retrieve':
        #     return TrackModification.objects.filter(order_id=self.request.order.id)
        # elif self.action == 'post' or self.action == 'destroy':
        #     return TrackModification.objects.filter(order_id=self.request.order.id)

        # return Order.objects.all()

    def get_serializer_class(self):
        try:
            if self.action == 'list':
                return OrderSerializer
            if self.action == 'retrieve':
                # TODO разобраться поч в админке не отображаются время создания и изменения
                return OrderSerializer
            if self.action == 'create':
                return OrderCreateSerializer
            elif self.action == 'destroy':
                return OrderSerializer
        # TODO почекать летят ли вообще ошибки
        except Exception as e:
            print(e)


# class VariationsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = TrackSerializers
#
#     def get_queryset(self):
#         print(list(Track.objects.filter(id=self.kwargs['pk']).values_list('variants', flat=True)))
#         variants = list(Track.objects.filter(id=self.kwargs['pk']).values_list('variants', flat=True))
#         return variants


@csrf_exempt
def order_api(request):
    if request.method == 'POST':
        order_data = JSONParser().parse(request)

        items = order_data.get('items')
        products_db = []

        for idx, item in enumerate(items):
            item_id = item.get('id')
            title = item.get('title')
            item_quantity = item.get('quantity')
            item_price = item.get('price')

            # 23:04 пример СМС
            # product = {'ID товара': item_id,
            #            'Название товара': title,
            #            'Количество': item_quantity,
            #            'Цена': item_price}

            # 23:23 пример СМС
            product = (f'{idx + 1}) ID товара: {item_id},'
                       f'\n - Название товара: {title},'
                       f'\n - Количество: {item_quantity},'
                       f'\n - Цена: {item_price},'
                       f'\n - Ссылка на сайте: http://nksgroup33.ru/product/{item_id},'
                       f'\n - Ссылка в админке: http://nksgroup33.ru:5000/admin/CatalogueApp/product/{item_id}/change/')
            products_db.append(product)

        order_data.pop('items')
        # print(products_db)
        products_db_str = json.dumps(products_db, ensure_ascii=False)
        order_data['products'] = products_db_str
        # order_data['products'] = products_db

        # print(products_db_str)

        # TODO сделать парсер чтоб приводить телефон к общему виду
        # order_client_phone = order_data.pop('phone')
        # order_client_email = order_data.pop('email')
        # client = None

        # if order_client_phone or order_client_email:
        #     client = Client.objects.filter(Q(phone=order_client_phone) | Q(email=order_client_email)).first()
        #     print(Client.objects.filter(Q(phone=order_client_phone) | Q(email=order_client_email)).query)
        #
        # order_data['client'] = client.id
        # order_name = order_data['name']


        order_serializer = OrderSerializers(data=order_data)


        if order_serializer.is_valid():
            saved_order = order_serializer.save()
            saved_order_id = saved_order.id

            delivery = order_data['delivery']
            total_price = order_data['price']
            client = order_data['name']
            number_phone = order_data['phone']
            products_formatted = '\n'.join(products_db)

            order_message = (f'Заказ №{saved_order_id}:'
                             f'\nФИО клиента: {client}.'
                             f'\nТелефон для связи: {number_phone}'
                             f'\nСумма заказа: {total_price} ₽'
                             f'\nСпособ доставки: {delivery}'
                             f'\nТовары:\n{products_formatted}')

            WhatsAppNotificator().send_message(order_message)
            # EmailNotificator().send_email(saved_order_id, order_message)

            return JsonResponse('Заказ оформлен', safe=False)

        return JsonResponse('Не удалось оформить заказ', safe=False)


class TrackReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
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
                if not item[0] == 'search':

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
        elif self.action == 'retrieve':
            return TrackSerializers


class FooterAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FooterSerializers
    queryset = Footer.objects.all()


class SubscriptionAPIView(generics.ListCreateAPIView):
    serializer_class = EmailSerializers
    queryset = User.objects.all()


class SubscriptionAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmailSerializers
    queryset = User.objects.all()


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


class TrackModificationModelViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        try:
            print(self.request.data)

            try:
                print('lold')
                order = Order.objects.get(id=self.request.data['order'])
                print('lol')
            except Order.DoesNotExist as e:
                print(type(e))
                order = None

            try:
                suggestive = SuggestiveEffect.objects.get(id=self.request.data['order'])
            except SuggestiveEffect.DoesNotExist as e:
                suggestive = None

            try:
                print('q')
                sport = Sports.objects.get(id=self.request.data['sports_name'])
                print('qw')
                # TODO такого не может быть
            except Sports.DoesNotExist as e:
                print(type(e))
                sport = None

            try:
                track = Track.objects.get(id=self.request.data['track'])
                # TODO такого не может быть
            except Track.DoesNotExist as e:
                print(type(e))
                track = None

            print(order)
            return serializer.save(order=order, track=track, sports_name=sport,
                                   suggestive_effect=suggestive)
        except Exception as e:
            print(e)
            raise APIException

    def get_queryset(self):
        # TODO разобраться мб понадобится
        # if self.action == 'list' or self.action == 'retrieve':
        #     return TrackModification.objects.filter(order_id=self.request.order.id)
        # elif self.action == 'post' or self.action == 'destroy':
        #     return TrackModification.objects.filter(order_id=self.request.order.id)

        return TrackModification.objects.all()

    def get_serializer_class(self):
        try:
            if self.action == 'list':
                return TrackModificationSerializer
            if self.action == 'retrieve':
                return TrackModificationSerializer
            if self.action == 'create':
                return TrackModificationCreateSerializers
            elif self.action == 'destroy':
                return TrackModificationDeleteSerializers
        # TODO почекать летят ли вообще ошибки
        except Exception as e:
            print(e)


class CustomTrackAPIView(generics.ListCreateAPIView):
    serializer_class = CustomTrackSerializers
    queryset = CustomTrack.objects.all()


class AddTrackToTheProgramAPIView(generics.ListCreateAPIView):
    serializer_class = AddTrackToTheProgramSerializers
    queryset = AddTrackToTheProgram.objects.all()


class AdBigPhotoFileViewSet(viewsets.ModelViewSet):
    serializer_class = AdBigPhotoFileSerializers
    queryset = AdBigPhotoFile.objects.all()


class AdSmallPhotoFileViewSet(viewsets.ModelViewSet):
    serializer_class = AdSmallPhotoFileSerializers
    queryset = AdSmallPhotoFile.objects.all()


class SuggestiveEffectViewSet(generics.ListCreateAPIView):
    serializer_class = SuggestiveEffectSerializers
    queryset = SuggestiveEffect.objects.all()


class UnloadingModule(viewsets.ModelViewSet):
    serializer_class = UnloadingModuleSerializers
    queryset = UnloadingModule.objects.all()


class WishlistModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            wished_track = Track.objects.get(id=self.request.data.get('id'))
            return serializer.save(user=self.request.user, wished_track=wished_track)
        except:
            raise NotFound

    def destroy(self, request, *args, **kwargs):
        wishlist_obj = self.get_queryset().get(wished_track__pk=int(request.data['track_id']))

        wishlist_obj.delete()

        return Response({'message': 'Трек удален из избранного'})

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


def get_filters_values(model_class, desired_fields, fields):
    filter_list = {}

    # сперва запускаем цикл по всем полям модельки
    for field in fields:
        field_name = field.name

        # проходимся только по необходимым для фильтров полям
        if field_name in desired_fields.values():
            filter_name_current = None

            # ищем корректное имя для фильтра чтоб передать на фронт
            for filter_name, desired_field_name in desired_fields.items():
                if desired_field_name == field_name:
                    filter_name_current = filter_name
                    break

            if isinstance(field, BooleanField):
                filter_list[filter_name_current] = {'type': 'checkbox',
                                                    'db_name': field_name,
                                                    'verbose_name': field.verbose_name}
            else:
                excludes = None

                if isinstance(field, ManyToManyField) or isinstance(field, ForeignKey):
                    empty_q = Q(**{f'{field_name}__isnull': True})
                    excludes = (excludes and (excludes | empty_q)) or empty_q
                    # TODO на фронте делать мультиселект для таких полей
                    pre_excluded_values = model_class.objects.order_by(field_name).values_list(field_name, flat=True).distinct()
                    values_minus_excluded = pre_excluded_values.exclude(excludes)
                    values = list(values_minus_excluded)

                    if field_name == "direction_music":
                        new_values = DirectionMusic.objects.filter(pk__in=values)
                        values_en = DirectionMusic.objects.values('direction_music_en')
                        name_en = 'Direction music'
                    elif field_name == "mood_name":
                        new_values = Moods.objects.filter(pk__in=values)
                        values_en = Moods.objects.values('mood_name_en')
                        name_en = 'Mood name'
                    elif field_name == "sports_name":
                        new_values = Sports.objects.filter(pk__in=values)
                        values_en = Sports.objects.values('sports_name_en')
                        name_en = 'Sports name'
                    elif field_name == "country_name":
                        new_values = Country.objects.filter(pk__in=values)
                        values_en = Country.objects.values('country_name_en')
                        name_en = 'Country name'
                    else:
                        new_values = None

                    if new_values:
                        new_values = list(new_values.annotate(title=F(field_name)).values('title', 'id'))
                        values_en = list(values_en.annotate(title=F(field_name + '_en')).values('title', 'id'))

                        filter_list[filter_name_current] = {'type': 'select',
                                                            'product_prop': field_name,
                                                            'name': field.verbose_name,
                                                            'name_en': name_en,
                                                            'values': new_values,
                                                            'values_en': values_en
                                                            }
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
                    values_en = list(values_minus_excluded)
                    name_en = 'Length'
                    if values:
                        filter_list[filter_name_current] = {'type': 'select',
                                                            'product_prop': field_name,
                                                            'name': field.verbose_name,
                                                            'name_en': name_en,
                                                            'values': values,
                                                            'values_en': values_en}

    return filter_list


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
        fields = [f for f in Track._meta.get_fields()]
        filter_field_names = {'sport': 'sports_name',
                              'len': 'track_length',
                              'direction': 'direction_music',
                              'character': 'mood_name',
                              'words': 'with_words',
                              'country': 'country_name'}

        fields_variant = get_filters_values(Track, filter_field_names, fields)

        return JsonResponse(fields_variant, safe=False)


def track_filtered(request):
    if request.method == 'GET':
        query_set = get_filtered_query_set(Track, request.GET.items())

        serializer = TrackSerializers(query_set, many=True)

        return JsonResponse(serializer.data, safe=False)


# def subscription_email(request):
#     if request.method == 'POST':
#         email_data = JSONParser().parse(request)
#         email_serializer = EmailSerializers(data=email_data)
#
#         if email_serializer.is_valid():
#             email_serializer.save()
#
#     elif request.method == 'GET':
#         subscription = MyUser.objects.all()
#         email_serializer = EmailSerializers(subscription, many=True)
#
#         return JsonResponse(email_serializer.data, safe=False)
#
#     elif request.method == 'PUT':
#         email_data = JSONParser().parse(request)
#
#         product = MyUser.objects.get(id=email_data['id'])
#         product_serializer = EmailSerializers(product, data=email_data)
#
#         if product_serializer.is_valid():
#             product_serializer.save()
#
#             return JsonResponse('Type Updated', safe=False)
#
#         return JsonResponse('Type to Update', safe=False)