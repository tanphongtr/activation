from rest_framework import serializers
from app.models import File
from app.utils import order_id_generate

class FileSerializer(serializers.ModelSerializer):

    file_name = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = '__all__'

    def get_file_name(self, obj):
        return obj.file.name