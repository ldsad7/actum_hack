from django.contrib.auth.models import User
from rest_framework import serializers

from procurements.models import Purchase


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
        # read_only_fields = fields

    author = serializers.SerializerMethodField()
    participants = serializers.SerializerMethodField()

    @staticmethod
    def get_author(instance: Purchase):
        return UserReadSerializer(instance.author).data

    @staticmethod
    def get_participants(instance: Purchase):
        return UserReadSerializer(instance.participants, many=True).data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User

    def to_representation(self, instance):
        return UserReadSerializer(instance).data


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User
        # read_only_fields = fields
