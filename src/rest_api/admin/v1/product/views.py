from rest_framework import generics, response
from app.models import Product
from django.db.models import Count, F, Value


from .serializers import ProductSerializer

class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TestProduct(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        product = Product.objects.filter(id=product_id, qty_remaining__gt=0)

        if not len(product):
            return response.Response({'error': 'Product not found'}, status=404)

        product.update(qty_remaining=F('qty_remaining') - 1)

        return response.Response({'success': 'Product is available'}, status=200)