from rest_framework import serializers
from app.models import Project
from app.utils import order_id_generate

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
