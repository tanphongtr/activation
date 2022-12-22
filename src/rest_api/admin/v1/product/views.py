from rest_framework import generics, response
from rest_framework.response import Response
from app.models import Product, Project
from django.db.models import Count, F, Value
from django.core.cache import cache
from django.db import transaction

from .serializers import ProductSerializer


class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TestProduct(generics.GenericAPIView):
    """
    Test product
    """

    @transaction.atomic
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        product = Product.objects.filter(id=product_id, qty_remaining__gt=0)
        if product.update(qty_remaining=F('qty_remaining') - 1):
            a = Project(
                name='test',
                created_by_id=1
            )
            a.save()

        return Response({'success': 'Product is available'}, status=200)
