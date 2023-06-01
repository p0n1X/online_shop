from rest_framework.views import APIView
from .models import Order, OrderDetail
from users.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer, OrderDetailSerializer
from carts.models import Cart
from datetime import datetime
from suppliers.models import Supplier
import logging


class OrderView(APIView):
    def get(self, request):
        try:
            user = User.objects.get(username=request.user)
        except User.DoesNotExist:
            logging.info('User is not login')
            Response(data={'message': 'User is not login'}, status=status.HTTP_204_NO_CONTENT)

        orders = Order.objects.filter(user=user)
        serialized = OrderSerializer(orders, many=True)
        return Response(data=serialized.data, status=status.HTTP_200_OK)

    def post(self, request):
        token = request.data.get('token', None)
        supplier_id = request.data.get('supplier', None)
        cart_items = Cart.objects.filter(token=token)
        total_price = 0
        for cart_item in cart_items:
            total_price += cart_item.product.price * cart_item.quantity
        try:
            supplier = Supplier.objects.get(id=supplier_id)
        except Supplier.DoesNotExist:
            logging.error('Invalid Supplier ID')
            return Response(data={'error': 'Invalid Supplier ID'}, status=status.HTTP_404_NOT_FOUND)

        total_price += supplier.price

        order_number = Order.objects.create(date=datetime.now(), total_price=total_price, user=cart_items[0].user, supplier=supplier)
        for cart_item in cart_items:
            OrderDetail.objects.create(order_number=order_number,
                                       product=cart_item.product,
                                       quantity=cart_item.quantity,
                                       price=cart_item.product.price)

        Cart.objects.filter(token=token).delete()
        logging.info('The Order was created successfully')
        return Response(data={'message': 'success'}, status=status.HTTP_200_OK)


class SingleOrderView(APIView):
    def get(self, request, id):
        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            logging.error('Invalid Supplier ID')
            return Response(data={'error': 'Invalid Order ID'}, status=status.HTTP_404_NOT_FOUND)

        orders = OrderDetail.objects.filter(order_number=order)
        serialized = OrderDetailSerializer(orders, many=True)
        return Response(data=serialized.data, status=status.HTTP_200_OK)
