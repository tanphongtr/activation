from rest_framework import generics, exceptions
from .serializers import FileSerializer
from app.models import File


class FileAPIView(generics.ListCreateAPIView):

    queryset = File.objects.all()
    serializer_class = FileSerializer

