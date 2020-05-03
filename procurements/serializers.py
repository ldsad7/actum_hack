from rest_framework import serializers

from procurements.models import Purchase, Producer, Country, ProductionType, ProductType, OKPD2ProductType, Material, \
    Colour, Characteristic, Product, Region, BaseUser, ContactPerson, Customer, Contractor, PurchaseMethod, \
    PurchaseType, ProductItem, Law, Offer, Contract, ContractorItem, CustomerItem


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Purchase

    def to_representation(self, instance):
        return PurchaseReadSerializer(instance).data


class PurchaseReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Purchase

    contractor_item = serializers.SerializerMethodField()
    participant_items = serializers.SerializerMethodField()
    product_items = serializers.SerializerMethodField()
    method = serializers.SerializerMethodField()
    law = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    offer = serializers.SerializerMethodField()

    @staticmethod
    def get_contractor_item(instance):
        if instance.contractor_item is not None:
            if instance.contractor_item is not None:
                return ContractorSerializer(instance.contractor_item.contractor).data

    @staticmethod
    def get_participant_items(instance):
        return CustomerSerializer([elem.customer for elem in instance.participant_items.all()], many=True).data

    @staticmethod
    def get_product_items(instance):
        return ProductSerializer([elem.product for elem in instance.product_items.all()], many=True).data

    @staticmethod
    def get_method(instance):
        return PurchaseMethodSerializer(instance.method).data

    @staticmethod
    def get_law(instance):
        if instance.law is not None:
            return LawSerializer(instance.law).data

    @staticmethod
    def get_type(instance):
        if instance.law is not None:
            return PurchaseTypeSerializer(instance.type).data

    @staticmethod
    def get_offer(instance):
        if instance.offer is not None:
            return OfferSerializer(instance.offer).data


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Producer

    def to_representation(self, instance):
        return ProducerReadSerializer(instance).data


class ProducerReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Producer


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Country

    def to_representation(self, instance):
        return CountryReadSerializer(instance).data


class CountryReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Country


class ProductionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProductionType

    def to_representation(self, instance):
        return ProductionTypeReadSerializer(instance).data


class ProductionTypeReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProductionType


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProductType

    def to_representation(self, instance):
        return ProductTypeReadSerializer(instance).data


class ProductTypeReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProductType


class OKPD2ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = OKPD2ProductType

    def to_representation(self, instance):
        return OKPD2ProductTypeReadSerializer(instance).data


class OKPD2ProductTypeReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = OKPD2ProductType


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Material

    def to_representation(self, instance):
        return MaterialReadSerializer(instance).data


class MaterialReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Material


class ColourSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Colour

    def to_representation(self, instance):
        return ColourReadSerializer(instance).data


class ColourReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Colour


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Characteristic

    def to_representation(self, instance):
        return CharacteristicReadSerializer(instance).data


class CharacteristicReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Characteristic


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product

    def to_representation(self, instance):
        return ProductReadSerializer(instance).data


class ProductReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product

    producer = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    production_type = serializers.SerializerMethodField()
    product_type = serializers.SerializerMethodField()
    okpd2_product_type = serializers.SerializerMethodField()
    characteristics = serializers.SerializerMethodField()
    material = serializers.SerializerMethodField()
    colour = serializers.SerializerMethodField()

    @staticmethod
    def get_producer(instance):
        if instance.producer is not None:
            return ProducerSerializer(instance.producer).data

    @staticmethod
    def get_country(instance):
        if instance.country is not None:
            return CountrySerializer(instance.country).data

    @staticmethod
    def get_production_type(instance):
        if instance.production_type is not None:
            return ProductionTypeSerializer(instance.production_type).data

    @staticmethod
    def get_product_type(instance):
        if instance.product_type is not None:
            return ProductTypeSerializer(instance.product_type).data

    @staticmethod
    def get_okpd2_product_type(instance):
        if instance.okpd2_product_type is not None:
            return OKPD2ProductTypeSerializer(instance.okpd2_product_type).data

    @staticmethod
    def get_characteristics(instance):
        return CharacteristicSerializer(instance.characteristics, many=True).data

    @staticmethod
    def get_material(instance):
        if instance.material is not None:
            return MaterialSerializer(instance.material).data

    @staticmethod
    def get_colour(instance):
        return ColourSerializer(instance.colour, many=True).data


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Region

    def to_representation(self, instance):
        return RegionReadSerializer(instance).data


class RegionReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Region


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = BaseUser

    def to_representation(self, instance):
        return BaseUserReadSerializer(instance).data


class BaseUserReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = BaseUser


class ContactPersonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ContactPerson

    def to_representation(self, instance):
        return ContactPersonReadSerializer(instance).data


class ContactPersonReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ContactPerson


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Customer

    def to_representation(self, instance):
        return CustomerReadSerializer(instance).data


class CustomerReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Customer

    contact_person = serializers.SerializerMethodField()
    registration_region = serializers.SerializerMethodField()
    production_types = serializers.SerializerMethodField()

    @staticmethod
    def get_contact_person(instance):
        if instance.contact_person is not None:
            return ContactPersonSerializer(instance).data

    @staticmethod
    def get_registration_region(instance):
        if instance.registration_region is not None:
            return RegionSerializer(instance.registration_region).data

    @staticmethod
    def get_production_types(instance):
        return ProductionTypeSerializer(instance.production_types, many=True).data


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Contractor

    def to_representation(self, instance):
        return ContractorReadSerializer(instance).data


class ContractorReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Contractor

    registration_region = serializers.SerializerMethodField()
    production_types = serializers.SerializerMethodField()

    @staticmethod
    def get_registration_region(instance):
        if instance.registration_region is not None:
            return RegionSerializer(instance.registration_region).data

    @staticmethod
    def get_production_types(instance):
        return ProductionTypeSerializer(instance.production_types, many=True).data

class PurchaseMethodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PurchaseMethod

    def to_representation(self, instance):
        return PurchaseMethodReadSerializer(instance).data


class PurchaseMethodReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PurchaseMethod


class PurchaseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PurchaseType

    def to_representation(self, instance):
        return PurchaseTypeReadSerializer(instance).data


class PurchaseTypeReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PurchaseType


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProductItem

    def to_representation(self, instance):
        return ProductItemReadSerializer(instance).data


class ProductItemReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProductItem


class LawSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Law

    def to_representation(self, instance):
        return LawReadSerializer(instance).data


class LawReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Law


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Offer

    def to_representation(self, instance):
        return OfferReadSerializer(instance).data


class OfferReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Offer


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Contract

    def to_representation(self, instance):
        return ContractReadSerializer(instance).data


class ContractReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Contract


class ContractorItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ContractorItem

    def to_representation(self, instance):
        return ContractorItemReadSerializer(instance).data


class ContractorItemReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ContractorItem


class CustomerItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CustomerItem

    def to_representation(self, instance):
        return CustomerItemReadSerializer(instance).data


class CustomerItemReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CustomerItem
