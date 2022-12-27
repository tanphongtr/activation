from django.urls import path, include
from .views import *

urlpatterns = [
    path('<int:product_id>/', TestFRedis.as_view()),
    path('test/<int:product_id>/', TestFRedis.as_view()),
    
]