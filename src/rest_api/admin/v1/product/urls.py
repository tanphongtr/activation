from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ProductAPIView.as_view(), name='product-list'),
    path('<int:product_id>/', TestProduct.as_view(), name='product-detail'),
]