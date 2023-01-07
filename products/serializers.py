from rest_framework import serializers
from .models import ProductInfo

# Serializers define the API representation.

# PriceSerializer defines the API representation for product info.
class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = ('id', 'name', 'price', 'description', 'quantity', 'is_available')
