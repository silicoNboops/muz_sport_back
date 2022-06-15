import django_filters
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import *


class TracksPagination(PageNumberPagination):
    page_size = 12

    def get_paginated_response(self, data):
        return Response({
            'product_count': self.page.paginator.count,
            'per_page': self.page_size,
            'page_count': self.page.paginator.num_pages,
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'results': data
        })


class NumberFilterInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class EmptyStringPlugFilter(filters.CharFilter):
    empty_value = 'EMPTY'

    def filter(self, qs, value):
        if value != self.empty_value:
            return super().filter(qs, value)

        qs = self.get_method(qs)(**{'%s__%s' % (self.field_name, self.lookup_expr): ""})
        return qs.distinct() if self.distinct else qs


class EmptyValueStringFilter(filters.BooleanFilter):
    def filter(self, qs, value):
        if value in [None, 'Не указано', 'Не задано', 'Любое', 'Пустое']:
            return qs

        exclude = self.exclude ^ (value is False)
        method = qs.exclude if exclude else qs.filter

        return method(**{self.field_name: ""})


class TracksFilter(filters.FilterSet):

    class Meta:
        model = Track
        fields = ['sports_name', 'tag_name', 'mood_name', 'with_words', 'country_name']


def get_client_ip(request):
    """Получение IP пользоваеля"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



