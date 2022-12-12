from rest_framework import serializers
from app.models import File
from app.utils import order_id_generate

class FileSerializer(serializers.ModelSerializer):

    file_name = serializers.SerializerMethodField(read_only=True)
    upload_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = File
        fields = ('id', 'file', 'file_name', 'upload_by', 'created_at')

    def get_file_name(self, obj):
        return obj.file.name