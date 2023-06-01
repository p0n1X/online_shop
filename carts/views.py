from rest_framework.views import APIView
from .models import Cart
from products.models import Product
from users.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartSerializer
import logging


class CartView(APIView):
    def get(self, request):
        try:
            user = User.objects.get(username=request.user)
        except User.DoesNotExist:
            logging.error('User is not login')
            return Response(data={'message': 'User is not login'}, status=status.HTTP_204_NO_CONTENT)
        cart = Cart.objects.filter(user=user, token=request.user.auth_token.key)
        serialized = CartSerializer(cart, many=True)
        return Response(data=serialized.data, status=status.HTTP_200_OK)

    def post(self, request):
        product_id = request.data.get('product')
        quantity = int(request.data.get('quantity'))
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            logging.error('Invalid Product ID')
            return Response(data={'error': 'Invalid Product ID'}, status=status.HTTP_404_NOT_FOUND)

        try:
            user = User.objects.get(username=request.user)
        except User.DoesNotExist:
            logging.error('User is not login')
            return Response(data={'message': 'User is not login'}, status=status.HTTP_204_NO_CONTENT)
        try:
            carts = Cart.objects.get(product=product, token=request.user.auth_token.key, user=user)
        except Cart.DoesNotExist:
            carts = Cart.objects.create(product=product, token=request.user.auth_token.key, user=user)

        carts.quantity = carts.quantity + quantity
        carts.save()
        logging.info(f'The Product {product.name} was added in cart successfully')
        return Response(data={'message': 'success'}, status=status.HTTP_200_OK)

    def delete(self, request):
        id = request.data.get('id')
        try:
            Cart.objects.get(id=id).delete()
        except Cart.DoesNotExist:
            logging.error('Wrong cart id')
            return Response(data={'message': 'Wrong cart id'}, status=status.HTTP_204_NO_CONTENT)

        logging.info('The Product was removed successfully')
        return Response(data={'message': 'Product was removed successfully'}, status=status.HTTP_200_OK)


