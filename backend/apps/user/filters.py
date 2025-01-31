from django_filters import rest_framework as filters


class UserFilter(filters.FilterSet):
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

    #phone
    phone_exact = filters.CharFilter(field_name='profile__phone', lookup_expr='exact')
    phone_startswith = filters.CharFilter(field_name='profile__phone', lookup_expr='startswith')
    phone_endswith = filters.CharFilter(field_name='profile__phone', lookup_expr='endswith')
    phone_contains = filters.CharFilter(field_name='profile__phone', lookup_expr='contains')


    # birthday
    birthday_date = filters.DateFilter(field_name='profile__birthday', lookup_expr='date')
    birthday_day = filters.DateFilter(field_name='profile__birthday', lookup_expr='day')
    birthday_month = filters.DateFilter(field_name='profile__birthday', lookup_expr='month')
    birthday_year = filters.DateFilter(field_name='profile__birthday', lookup_expr='year')

    #age
    age_gt = filters.NumberFilter(field_name='profile__age', lookup_expr='gt')
    age_gte = filters.NumberFilter(field_name='profile__age', lookup_expr='gte')
    age_lt = filters.NumberFilter(field_name='profile__age', lookup_expr='lt')
    age_lte = filters.NumberFilter(field_name='profile__age', lookup_expr='lte')
    age_in = filters.BaseInFilter(field_name='profile__age')
    age_range = filters.RangeFilter(field_name='profile__age')







