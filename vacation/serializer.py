from rest_framework import serializers

from .models import Villa, Yacht, Vehicle


class VillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Villa
        fields = ['title', 'description', 'price_per_day', 'exist']


class YachtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yacht
        fields = ['title', 'length', 'price_per_day', 'exist']


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['title', 'color', 'price_per_day', 'exist']
