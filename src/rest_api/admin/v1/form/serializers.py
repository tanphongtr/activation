from rest_framework import serializers
from form.models import Form, FormGroup, FormField, FieldOption, FieldType


class FieldTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FieldType
        fields = '__all__'
        # read_only_fields = ('id',)

class FieldOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = FieldOption
        fields = '__all__'
        # read_only_fields = ('id',)


class FormFieldSerializer(serializers.ModelSerializer):

    options = FieldOptionSerializer(many=True, read_only=True)
    field_type = FieldTypeSerializer(many=False, read_only=True)

    class Meta:
        model = FormField
        fields = '__all__'
        # read_only_fields = ('id',)


# Child of FormSerializer
class FormGroupSerializer(serializers.ModelSerializer):

    form_fields = FormFieldSerializer(many=True, read_only=True)

    class Meta:
        model = FormGroup
        fields = '__all__'
        # read_only_fields = ('id',)


class FormSerializer(serializers.ModelSerializer):

    form_groups = FormGroupSerializer(many=True, read_only=True)

    class Meta:
        model = Form
        fields = '__all__'
        # read_only_fields = ('id',)