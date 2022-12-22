from rest_framework import generics
from form.models import Form
from .serializers import FormSerializer


class FormAPIView(generics.ListAPIView):

    queryset = Form.objects.all()
    serializer_class = FormSerializer

    def get(self, request, *args, **kwargs):
        print('FormAPIView get')
        
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class FormDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Form.objects.all()
    serializer_class = FormSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
