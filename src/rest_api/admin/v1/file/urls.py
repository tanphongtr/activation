from django.urls import path
from .views import *


urlpatterns = [
    path('', FileAPIView.as_view()),
]