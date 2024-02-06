from django.contrib.auth.hashers import make_password
from django.test import TestCase
from datetime import datetime

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status

from carts.models import Cart
from categories.models import Category
from products.models import Product
from suppliers.models import Supplier
from users.models import User
from .models import Order, OrderDetail


class OrderTest(TestCase):
    def setUp(self) -> None:
        self.date = datetime.now()
        self.category_tv = Category.objects.create(name='category_tv_test')
        self.category_laptop = Category.objects.create(name='category_laptop_test')
        self.supplier = Supplier.objects.create(name='supplier_test', price=32)
        self.product_tv = Product.objects.create(name='product_tv_test',
                                                 active=True,
                                                 sku_number=4523532,
                                                 description='product tv description',
                                                 quantity=5,
                                                 category=self.category_tv,
                                                 price=435.56)
        self.product_laptop = Product.objects.create(name='product_laptop_test',
                                                     active=True,
                                                     sku_number=53453,
                                                     description='product laptop description',
                                                     quantity=15,
                                                     category=self.category_laptop,
                                                     price=1234.56)

        self.user = User.objects.create(username='username_test',
                                        first_name='John',
                                        last_name='Doe',
                                        address='Plovdiv',
                                        email='john.doe@jonhmail.com',
                                        password=make_password('test_pass'))

    def test_post_order(self):
        order = Order.objects.create(date=self.date,
                                     total_price=423423,
                                     user=self.user,
                                     supplier=self.supplier)

        order_details_tv = OrderDetail.objects.create(order_number=order,
                                                      product=self.product_tv,
                                                      quantity=3,
                                                      price=65)

        order_details_laptop = OrderDetail.objects.create(order_number=order,
                                                          product=self.product_laptop,
                                                          quantity=2,
                                                          price=78)

        self.assertEquals('username_test', order.user.username)
        self.assertEquals(self.date, order.date)
        self.assertEquals(423423, order.total_price)
        self.assertEquals('supplier_test', order.supplier.name)
        self.assertEquals('product_tv_test', order_details_tv.product.name)
        self.assertEquals(65, order_details_tv.price)
        self.assertEquals(3, order_details_tv.quantity)

        self.assertEquals('product_laptop_test', order_details_laptop.product.name)
        self.assertEquals(78, order_details_laptop.price)
        self.assertEquals(2, order_details_laptop.quantity)


class OrderApiTest(TestCase):
    def setUp(self) -> None:
        self.order_url = '/api/orders'
        self.client = APIClient()
        self.date = datetime.now()
        self.category_tv = Category.objects.create(name='category_tv_test')
        self.category_laptop = Category.objects.create(name='category_laptop_test')
        self.supplier = Supplier.objects.create(name='supplier_test', price=32)
        self.product_tv = Product.objects.create(name='product_tv_test',
                                                 active=True,
                                                 sku_number=4523532,
                                                 description='product tv description',
                                                 quantity=5,
                                                 category=self.category_tv,
                                                 price=435.56)
        self.product_laptop = Product.objects.create(name='product_laptop_test',
                                                     active=True,
                                                     sku_number=53453,
                                                     description='product laptop description',
                                                     quantity=15,
                                                     category=self.category_laptop,
                                                     price=1234.56)

        self.user = User.objects.create(username='username_test',
                                        first_name='John',
                                        last_name='Doe',
                                        address='Plovdiv',
                                        email='john.doe@jonhmail.com',
                                        password=make_password('test_pass'))

        self.token = Token.objects.create(user=self.user)

        Cart.objects.create(product=self.product_tv,
                            user=self.user,
                            quantity=4,
                            token=self.token)

        Cart.objects.create(product=self.product_laptop,
                            user=self.user,
                            quantity=2,
                            token=self.token)

    def test_post_order(self):
        payload = {
            'token': self.token,
            'supplier': self.supplier.id
        }
        result = self.client.post(f'{self.order_url}/', payload)
        self.assertEquals(result.status_code, status.HTTP_200_OK)
        self.assertEquals(result.data['message'], 'The Order was created successfully')

        get_order = self.client.get(f'{self.order_url}/', **{"HTTP_AUTHORIZATION": f"Token {self.token}"})
        self.assertEquals(get_order.status_code, status.HTTP_200_OK)
        self.assertEquals(len(get_order.data), 1)

        get_order_details = self.client.get(f'{self.order_url}/{get_order.data[0].get("id")}')
        self.assertEquals(get_order_details.status_code, status.HTTP_200_OK)
        self.assertEquals(len(get_order_details.data), 2)
        self.assertEquals(get_order_details.data[0].get('name'), 'product_tv_test')
        self.assertEquals(get_order_details.data[0].get('description'), 'product tv description')
