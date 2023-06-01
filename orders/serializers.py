from rest_framework import serializers
from .models import Order, OrderDetail


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        serialized_data = super(OrderSerializer, self).to_representation(instance)
        serialized_data['supplier'] = instance.supplier.name

        return serialized_data


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

    def to_representation(self, instance):
        serialized_data = super(OrderDetailSerializer, self).to_representation(instance)
        serialized_data['name'] = instance.product.name
        serialized_data['description'] = instance.product.description
        serialized_data['date'] = instance.order_number.date
        serialized_data['sku_number'] = instance.product.sku_number
        serialized_data['category'] = instance.product.category.name
        serialized_data['price'] = instance.product.price

        return serialized_data
