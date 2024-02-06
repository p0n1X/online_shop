import logging
from datetime import datetime
from .models import Order, OrderDetail
from .serializers import OrderSerializer, OrderDetailSerializer
from carts.models import Cart
from suppliers.supplier import SupplierController
from users.user import UserController


class OrderController:

    @staticmethod
    def get_orders(user):
        user = UserController.get_user_by_id(user.id)
        orders = Order.objects.filter(user=user).order_by('-id')
        serialized = OrderSerializer(orders, many=True)
        return serialized.data

    @staticmethod
    def create_order(token, supplier_id):
        cart_items = Cart.objects.filter(token=token)
        total_price = 0
        for cart_item in cart_items:
            total_price += cart_item.product.price * cart_item.quantity

        supplier = SupplierController.get_suppliers_by_id(supplier_id)
        total_price += supplier.price
        order_number = Order.objects.create(date=datetime.now(), total_price=total_price, user=cart_items[0].user,
                                            supplier=supplier)
        for cart_item in cart_items:
            OrderDetail.objects.create(order_number=order_number,
                                       product=cart_item.product,
                                       quantity=cart_item.quantity,
                                       price=cart_item.product.price)

        Cart.objects.filter(token=token).delete()
        logging.info('The Order was created successfully')

    @staticmethod
    def get_order(id):
        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            logging.error('Invalid Supplier ID')
            raise ValueError('Invalid Order ID')

        orders = OrderDetail.objects.filter(order_number=order)
        serialized = OrderDetailSerializer(orders, many=True)

        return serialized.data