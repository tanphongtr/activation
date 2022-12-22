from rest_framework import serializers
from app.models import Product
from django.db.models import Count, F, Value


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


    def update_qty_remaining(self):
        self.qty_remaining = F('qty_remaining') - 1
        self.save()

        return self