from django.urls import path, include
from .views import *

urlpatterns = [
    path('', FormAPIView.as_view(), name='form-list'),
    path('<int:pk>/', FormDetailAPIView.as_view(), name='form-detail'),
]