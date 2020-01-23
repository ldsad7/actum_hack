from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from procurements.exceptions import NoSuchId
from procurements.filters import PurchaseFilter
from procurements.models import Purchase
from procurements.serializers import UserSerializer, UserReadSerializer, PurchaseSerializer


class PurchaseViewSet(ModelViewSet):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all().prefetch_related('user')
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = PurchaseFilter
    ordering_fields = ('name',)


class AuthorViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=True, methods=['get'])
    def purchases(self, request, pk):
        try:
            author_obj = User.objects.get(id=pk)
        except User.DoesNotExist:
            raise NoSuchId()
        purchases = self.paginate_queryset(Purchase.objects.filter(author=author_obj))
        return self.get_paginated_response(data=UserReadSerializer(purchases, many=True).data)
