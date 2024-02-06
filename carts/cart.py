import logging
from .models import Cart
from .serializers import CartSerializer
from products.product import ProductController
from users.user import UserController


class CartController:

    @staticmethod
    def get_items(user):
        user = UserController.get_user_by_id(user.id)
        if user is None:
            return None
        cart = Cart.objects.filter(user=user, token=user.auth_token.key)
        serialized = CartSerializer(cart, many=True)
        return serialized.data

    @staticmethod
    def add_item(product_id, quantity, user):
        product = ProductController.get_product_by_id(product_id)
        user = UserController.get_user_by_id(user.id)
        try:
            carts = Cart.objects.get(product=product, token=user.auth_token.key, user=user)
        except Cart.DoesNotExist:
            carts = Cart.objects.create(product=product, token=user.auth_token.key, user=user)

        carts.quantity = carts.quantity + quantity
        carts.save()
        logging.info(f'The Product {product.name} was added in cart successfully')

    @staticmethod
    def remove_item(id):
        try:
            Cart.objects.get(id=id).delete()
        except Cart.DoesNotExist:
            logging.error('Wrong cart id')
            raise ValueError('Wrong cart id')

        logging.info('The Product was removed successfully')
