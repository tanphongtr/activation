from rest_framework import generics, exceptions
from .serializers import ProjectSerializer
from app.models import Project
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
# import permission
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.permissions import DjangoModelPermissions, BasePermission, SAFE_METHODS

class RoutePermissions(DjangoModelPermissions):

    def __init__(self) -> None:
        super().__init__()
        self.request = None

    perms_map = {
        'GET': ['route.get_%(view_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['route.post_%(view_name)s'],
        'PUT': ['route.update_%(view_name)s'],
        'PATCH': ['route.update_%(view_name)s'],
        'DELETE': ['route.delete_%(view_name)s'],
    }

    def has_permission(self, request, view):
        self.request = request
        return super().has_permission(request, view)

    def get_required_permissions(self, method, model_cls):
        """
        Given a model and an HTTP method, return the list of permission
        codes that the user is required to have.
        """
        kwargs = {
            'view_name': self.request.resolver_match.view_name
        }

        if method not in self.perms_map:
            raise exceptions.MethodNotAllowed(method)

        return [perm % kwargs for perm in self.perms_map[method]]


class ProjectAPIView(generics.ListCreateAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [RoutePermissions, IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def perform_create(self, serializer):
        try:
            serializer.save()
        except Exception as e:
            raise exceptions.APIException(detail=str(e))

    def get(self, request, *args, **kwargs):
        name = self.request.resolver_match.view_name
        print(name)
        return super().get(request, *args, **kwargs)