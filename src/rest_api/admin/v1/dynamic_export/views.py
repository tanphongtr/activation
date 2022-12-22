from rest_framework import viewsets, response, generics, exceptions
from django.apps import apps
from .serializers import DynamicExportSerializer

class DynamicExportAPIView(generics.GenericAPIView):

    serializer_class = DynamicExportSerializer

    def get_model(self):
        model_name = self.request.data.get('model_name')

        try:
            model = apps.get_model('app', model_name)
        except LookupError:
            raise exceptions.APIException(f'Model not found, {LookupError}')

        return model

    def get_queryset(self):
        model = self.get_model()
        return model.objects.all()

    def get_serializer_class(self):
        model = self.get_model()
        self.serializer_class.Meta.model = model
        return self.serializer_class

    def get_serializer_class(self):
        return super().get_serializer_class()

    def post(self, request, *args, **kwargs):
        model_name = request.data.get('model_name')
        fields = request.data.get('fields')
        model = self.get_model()
        self.serializer_class.Meta.model = model
        serializer = self.get_serializer(
            model.objects.all(),
            many=True,
            context={'request': request},
            fields=fields
        )
        return response.Response(serializer.data)