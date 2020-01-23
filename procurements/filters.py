# from procurements.models import Purchase
import django_filters as filters


class PurchaseFilter(filters.FilterSet):
    name = filters.CharFilter('name', 'icontains')
    author_id = filters.BaseInFilter('author_id')
    is_active = filters.BooleanFilter('is_active')
    is_deleted = filters.BooleanFilter('is_deleted')
