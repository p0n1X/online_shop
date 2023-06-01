from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        serialized_data = super(ProductSerializer, self).to_representation(instance)
        serialized_data['category_id'] = instance.category.id
        serialized_data['category'] = instance.category.name

        return serialized_data
