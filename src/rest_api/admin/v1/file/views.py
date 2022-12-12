from rest_framework import generics, exceptions
from .serializers import FileSerializer
from app.models import File
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser


class FileAPIView(generics.CreateAPIView):

    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser,)

    # def perform_create(self, serializer):
    #     serializer.save(upload_by=self.request.user)

