from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
# from gensim.models import Word2Vec
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from procurements.exceptions import NoSuchParameter, NoWordInModel
from procurements.filters import PurchaseFilter, ProductFilter
from procurements.models import Purchase, Producer, Country, ProductionType, ProductType, OKPD2ProductType, Material, \
    Colour, Characteristic, Product, Region, BaseUser, ContactPerson, Customer, Contractor, PurchaseMethod, \
    PurchaseType, ProductItem, Law, Offer, Contract, ContractorItem, CustomerItem
from procurements.serializers import PurchaseSerializer, ProducerSerializer, CountrySerializer, \
    ProductionTypeSerializer, ProductTypeSerializer, OKPD2ProductTypeSerializer, MaterialSerializer, ColourSerializer, \
    CharacteristicSerializer, ProductSerializer, RegionSerializer, BaseUserSerializer, ContactPersonSerializer, \
    CustomerSerializer, ContractorSerializer, PurchaseMethodSerializer, PurchaseTypeSerializer, ProductItemSerializer, \
    LawSerializer, OfferSerializer, ContractSerializer, ContractorItemSerializer, CustomerItemSerializer

# search_model = Word2Vec.load('modelName.model')


def index(request):
    return render(request, 'index.html')


class PurchaseViewSet(ModelViewSet):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all().prefetch_related(
        'contractor_item__contractor', 'participant_items__customer', 'product_items__product'
    )
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
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = ProductFilter
    ordering_fields = ('name',)

    # @action(detail=False, methods=['get'])
    # def search(self, request):
    #     """
    #     query: string to search for
    #     n: number of results to return
    #     :param request:
    #     :return:
    #     """

    #     filter_query = request.GET.get('query')
    #     filter_n = int(float(request.GET.get('n', 10)))
    #     if not filter_query:
    #         raise NoSuchParameter("No 'query' field in request")
    #     try:
    #         word_vector = search_model.wv[filter_query.capitalize()]
    #     except KeyError:
    #         try:
    #             word_vector = search_model.wv[filter_query.lower()]
    #         except KeyError:
    #             raise NoWordInModel()

    #     return Response(
    #         data=[
    #             {'name': pair[0], 'value': pair[1]}
    #             for pair in search_model.similar_by_vector(word_vector, topn=filter_n)
    #         ], status=200
    #     )


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
    queryset = ProductItem.objects.all().prefetch_related('product')


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
