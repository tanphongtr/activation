from rest_framework import generics, exceptions
from .serializers import ProjectSerializer
from app.models import Project


class ProjectAPIView(generics.ListCreateAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        try:
            serializer.save()
        except Exception as e:
            raise exceptions.APIException(detail=str(e))