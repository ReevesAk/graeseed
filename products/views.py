from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import ProductInfo
from products.serializers import ProductInfoSerializer


# Create your views here.

@api_view(['GET'])
def getAllProducts(request):
    products = ProductInfo.objects.all()
    serializer = ProductInfoSerializer(products, many=True)
    return Response(serializer.data)