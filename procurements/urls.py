from django.urls import path, include
from rest_framework.routers import DefaultRouter


from procurements.views import PurchaseViewSet, ProducerViewSet, CountryViewSet, \
    ProductionTypeViewSet, ProductTypeViewSet, OKPD2ProductTypeViewSet, MaterialViewSet, ColourViewSet, \
    CharacteristicViewSet, ProductViewSet, RegionViewSet, BaseUserViewSet, ContactPersonViewSet, \
    CustomerViewSet, ContractorViewSet, PurchaseMethodViewSet, PurchaseTypeViewSet, ProductItemViewSet, \
    LawViewSet, OfferViewSet, ContractViewSet, ContractorItemViewSet, CustomerItemViewSet

api_router = DefaultRouter()
api_router.register('purchases', PurchaseViewSet, 'purchases')
api_router.register('products', ProducerViewSet, 'products')
api_router.register('countries', CountryViewSet, 'countries')
api_router.register('production_types', ProductionTypeViewSet, 'production_types')
api_router.register('product_types', ProductTypeViewSet, 'product_types')
api_router.register('okpd2_product_types', OKPD2ProductTypeViewSet, 'okpd2_product_types')
api_router.register('materials', MaterialViewSet, 'materials')
api_router.register('colours', ColourViewSet, 'colours')
api_router.register('characteristics', CharacteristicViewSet, 'characteristics')
api_router.register('products', ProductViewSet, 'products')
api_router.register('regions', RegionViewSet, 'regions')
api_router.register('base_users', BaseUserViewSet, 'base_users')
api_router.register('contact_persons', ContactPersonViewSet, 'contact_persons')
api_router.register('customers', CustomerViewSet, 'customers')
api_router.register('contractors', ContractorViewSet, 'contractors')
api_router.register('purchase_methods', PurchaseMethodViewSet, 'purchase_methods')
api_router.register('purchase_types', PurchaseTypeViewSet, 'purchase_types')
api_router.register('product_items', ProductItemViewSet, 'product_items')
api_router.register('laws', LawViewSet, 'laws')
api_router.register('offers', OfferViewSet, 'offers')
api_router.register('contracts', ContractViewSet, 'contracts')
api_router.register('contractor_items', ContractorItemViewSet, 'contractor_items')
api_router.register('customer_items', CustomerItemViewSet, 'customer_items')

urlpatterns = [
    path('', include(api_router.urls)),
]
