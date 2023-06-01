from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

    def to_representation(self, instance):
        serialized_data = super(CartSerializer, self).to_representation(instance)
        serialized_data['product'] = instance.product.name
        serialized_data['product_id'] = instance.product.id
        serialized_data['user'] = instance.user.username
        serialized_data['firstname'] = instance.user.first_name
        serialized_data['lastname'] = instance.user.last_name
        serialized_data['address'] = instance.user.address
        serialized_data['email'] = instance.user.email
        serialized_data['price'] = instance.product.price
        serialized_data['total_price'] = instance.product.price * instance.quantity

        return serialized_data
