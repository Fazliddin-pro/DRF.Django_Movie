from django_filters import rest_framework as filters
from .models import Movie

def get_client_ip(self, request):
    """Получение IP адреса"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class MovieFilter(filters.FilterSet):
    """Фильтры для фильмов"""
    genres = CharFilterInFilter(field_name='genres__slug', lookup_expr='in')
    directors = CharFilterInFilter(field_name='directors__slug', lookup_expr='in')
    actors = CharFilterInFilter(field_name='actors__slug', lookup_expr='in')
    year = filters.RangeFilter()

    class Meta:
        model = Movie
        fields = ('genres', 'directors', 'actors', 'year')