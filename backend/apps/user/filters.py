from django_filters import rest_framework as filters

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserFilter(filters.FilterSet):
    # user
    # id
    id_gt = filters.NumberFilter(field_name='id', lookup_expr='gt')
    id_gte = filters.NumberFilter(field_name='id', lookup_expr='gte')
    id_lt = filters.NumberFilter(field_name='id', lookup_expr='lt')
    id_lte = filters.NumberFilter(field_name='id', lookup_expr='lte')
    id_in = filters.BaseInFilter(field_name='id')
    id_range = filters.RangeFilter(field_name='id')

    # email
    email_exact = filters.CharFilter(field_name='email', lookup_expr='exact')
    email_startswith = filters.CharFilter(field_name='email', lookup_expr='startswith')
    email_endswith = filters.CharFilter(field_name='email', lookup_expr='endswith')
    email_contains = filters.CharFilter(field_name='email', lookup_expr='contains')

    # profile
    # name
    name_exact = filters.CharFilter(field_name='profile__name', lookup_expr='exact')
    name_iexact = filters.CharFilter(field_name='profile__name', lookup_expr='iexact')
    name_startswith = filters.CharFilter(field_name='profile__name', lookup_expr='startswith')
    name_istartswith = filters.CharFilter(field_name='profile__name', lookup_expr='istartswith')
    name_endswith = filters.CharFilter(field_name='profile__name', lookup_expr='endswith')
    name_iendswith = filters.CharFilter(field_name='profile__name', lookup_expr='iendswith')
    name_contains = filters.CharFilter(field_name='profile__name', lookup_expr='contains')
    name_icontains = filters.CharFilter(field_name='profile__name', lookup_expr='icontains')

    # surname
    surname_exact = filters.CharFilter(field_name='profile__surname', lookup_expr='exact')
    surname_iexact = filters.CharFilter(field_name='profile__surname', lookup_expr='iexact')
    surname_startswith = filters.CharFilter(field_name='profile__surname', lookup_expr='startswith')
    surname_istartswith = filters.CharFilter(field_name='profile__surname', lookup_expr='istartswith')
    surname_endswith = filters.CharFilter(field_name='profile__surname', lookup_expr='endswith')
    surname_iendswith = filters.CharFilter(field_name='profile__surname', lookup_expr='iendswith')
    surname_contains = filters.CharFilter(field_name='profile__surname', lookup_expr='contains')
    surname_icontains = filters.CharFilter(field_name='profile__surname', lookup_expr='icontains')

    # phone
    phone_exact = filters.CharFilter(field_name='profile__phone', lookup_expr='exact')
    phone_startswith = filters.CharFilter(field_name='profile__phone', lookup_expr='startswith')
    phone_endswith = filters.CharFilter(field_name='profile__phone', lookup_expr='endswith')
    phone_contains = filters.CharFilter(field_name='profile__phone', lookup_expr='contains')

    # birthday
    birthday_date = filters.DateFilter(field_name='profile__birthday', lookup_expr='date')
    birthday_day = filters.NumberFilter(field_name='profile__birthday', lookup_expr='day')
    birthday_month = filters.NumberFilter(field_name='profile__birthday', lookup_expr='month')
    birthday_year = filters.NumberFilter(field_name='profile__birthday', lookup_expr='year')

    # age
    age_gt = filters.NumberFilter(field_name='profile__age', lookup_expr='gt')
    age_gte = filters.NumberFilter(field_name='profile__age', lookup_expr='gte')
    age_lt = filters.NumberFilter(field_name='profile__age', lookup_expr='lt')
    age_lte = filters.NumberFilter(field_name='profile__age', lookup_expr='lte')
    age_in = filters.BaseInFilter(field_name='profile__age')
    age_range = filters.RangeFilter(field_name='profile__age')

    # city
    city_exact = filters.CharFilter(field_name='profile__city', lookup_expr='exact')
    city_iexact = filters.CharFilter(field_name='profile__city', lookup_expr='iexact')
    city_startswith = filters.CharFilter(field_name='profile__city', lookup_expr='startswith')
    city_istartswith = filters.CharFilter(field_name='profile__city', lookup_expr='istartswith')
    city_endswith = filters.CharFilter(field_name='profile__city', lookup_expr='endswith')
    city_iendswith = filters.CharFilter(field_name='profile__city', lookup_expr='iendswith')
    city_contains = filters.CharFilter(field_name='profile__city', lookup_expr='contains')
    city_icontains = filters.CharFilter(field_name='profile__city', lookup_expr='icontains')

    # country
    country_exact = filters.CharFilter(field_name='profile__country', lookup_expr='exact')
    country_iexact = filters.CharFilter(field_name='profile__country', lookup_expr='iexact')
    country_startswith = filters.CharFilter(field_name='profile__country', lookup_expr='startswith')
    country_istartswith = filters.CharFilter(field_name='profile__country', lookup_expr='istartswith')
    country_endswith = filters.CharFilter(field_name='profile__country', lookup_expr='endswith')
    country_iendswith = filters.CharFilter(field_name='profile__country', lookup_expr='iendswith')
    country_contains = filters.CharFilter(field_name='profile__country', lookup_expr='contains')
    country_icontains = filters.CharFilter(field_name='profile__country', lookup_expr='icontains')

    # nationality
    nationality_exact = filters.CharFilter(field_name='profile__nationality', lookup_expr='exact')
    nationality_iexact = filters.CharFilter(field_name='profile__nationality', lookup_expr='iexact')
    nationality_startswith = filters.CharFilter(field_name='profile__nationality', lookup_expr='startswith')
    nationality_istartswith = filters.CharFilter(field_name='profile__nationality', lookup_expr='istartswith')
    nationality_endswith = filters.CharFilter(field_name='profile__nationality', lookup_expr='endswith')
    nationality_iendswith = filters.CharFilter(field_name='profile__nationality', lookup_expr='iendswith')
    nationality_contains = filters.CharFilter(field_name='profile__nationality', lookup_expr='contains')
    nationality_icontains = filters.CharFilter(field_name='profile__nationality', lookup_expr='icontains')

    class Meta:
        model = UserModel
        fields = {
            'id': ['exact'],
            'email': ['exact', 'icontains'],
        }
