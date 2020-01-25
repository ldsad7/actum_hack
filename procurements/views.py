from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from procurements.filters import PurchaseFilter
from procurements.models import Purchase, Producer, Country, ProductionType, ProductType, OKPD2ProductType, Material, \
    Colour, Characteristic, Product, Region, BaseUser, ContactPerson, Customer, Contractor, PurchaseMethod, \
    PurchaseType, ProductItem, Law, Offer, Contract, ContractorItem, CustomerItem
from procurements.serializers import PurchaseSerializer, ProducerSerializer, CountrySerializer, \
    ProductionTypeSerializer, ProductTypeSerializer, OKPD2ProductTypeSerializer, MaterialSerializer, ColourSerializer, \
    CharacteristicSerializer, ProductSerializer, RegionSerializer, BaseUserSerializer, ContactPersonSerializer, \
    CustomerSerializer, ContractorSerializer, PurchaseMethodSerializer, PurchaseTypeSerializer, ProductItemSerializer, \
    LawSerializer, OfferSerializer, ContractSerializer, ContractorItemSerializer, CustomerItemSerializer


class PurchaseViewSet(ModelViewSet):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all().prefetch_related('user')
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = PurchaseFilter
    ordering_fields = ('name',)


class ProducerViewSet(ModelViewSet):
    serializer_class = ProducerSerializer
    queryset = Producer.objects.all()


class CountryViewSet(ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class ProductionTypeViewSet(ModelViewSet):
    serializer_class = ProductionTypeSerializer
    queryset = ProductionType.objects.all()


class ProductTypeViewSet(ModelViewSet):
    serializer_class = ProductTypeSerializer
    queryset = ProductType.objects.all()


class OKPD2ProductTypeViewSet(ModelViewSet):
    serializer_class = OKPD2ProductTypeSerializer
    queryset = OKPD2ProductType.objects.all()


class MaterialViewSet(ModelViewSet):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class ColourViewSet(ModelViewSet):
    serializer_class = ColourSerializer
    queryset = Colour.objects.all()


class CharacteristicViewSet(ModelViewSet):
    serializer_class = CharacteristicSerializer
    queryset = Characteristic.objects.all()


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class RegionViewSet(ModelViewSet):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class BaseUserViewSet(ModelViewSet):
    serializer_class = BaseUserSerializer
    queryset = BaseUser.objects.all()


class ContactPersonViewSet(ModelViewSet):
    serializer_class = ContactPersonSerializer
    queryset = ContactPerson.objects.all()


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class ContractorViewSet(ModelViewSet):
    serializer_class = ContractorSerializer
    queryset = Contractor.objects.all()


class PurchaseMethodViewSet(ModelViewSet):
    serializer_class = PurchaseMethodSerializer
    queryset = PurchaseMethod.objects.all()


class PurchaseTypeViewSet(ModelViewSet):
    serializer_class = PurchaseTypeSerializer
    queryset = PurchaseType.objects.all()


class ProductItemViewSet(ModelViewSet):
    serializer_class = ProductItemSerializer
    queryset = ProductItem.objects.all()


class LawViewSet(ModelViewSet):
    serializer_class = LawSerializer
    queryset = Law.objects.all()


class OfferViewSet(ModelViewSet):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()


class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()


class ContractorItemViewSet(ModelViewSet):
    serializer_class = ContractorItemSerializer
    queryset = ContractorItem.objects.all()


class CustomerItemViewSet(ModelViewSet):
    serializer_class = CustomerItemSerializer
    queryset = CustomerItem.objects.all()
