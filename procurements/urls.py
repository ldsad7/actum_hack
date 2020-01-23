from django.urls import path, include
from rest_framework.routers import DefaultRouter

from procurements.views import PurchaseViewSet, AuthorViewSet

api_router = DefaultRouter()
api_router.register('purchases', PurchaseViewSet, 'purchases')
api_router.register('authors', AuthorViewSet, 'authors')

urlpatterns = [
    path('', include(api_router.urls)),
]
