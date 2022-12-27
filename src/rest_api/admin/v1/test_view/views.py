from rest_framework import generics
from rest_framework.response import Response
from django.db import transaction
from django.db.models import F
from app.models import Product, Project
from django.core.cache import cache


class TestF(generics.GenericAPIView):
    """
    Test product
    """

    @transaction.atomic
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        product = Product.objects.filter(id=product_id, qty_remaining__gt=0)
        if product.update(qty_remaining=F('qty_remaining') - 1):
            # thêm một vài đoạn code ở đây
            print('ok')
            pass

        return Response({'success': 'Product is available'}, status=200)


class TestFRedis(generics.GenericAPIView):
    """
    Test product
    """

    def get(self, request, *args, **kwargs):

        print('====')

        return Response({'success': 'Product is available'}, status=200)