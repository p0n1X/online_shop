from django.test import TestCase
from .models import Cart
from products.models import Product
from categories.models import Category
from users.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token


class CartTest(TestCase):
    def setUp(self) -> None:
        self.category_tv = Category.objects.create(name='category_tv_test')
        self.category_laptop = Category.objects.create(name='category_laptop_test')
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

    def test_post_cart(self):
        cart = Cart.objects.create(product=self.product_tv,
                                   user=self.user,
                                   quantity=4,
                                   token=self.token)

        self.assertEquals('product_tv_test', cart.product.name)
        self.assertEquals('username_test', cart.user.username)
        self.assertEquals(4, cart.quantity)
        self.assertEquals(self.token, cart.token)

    def test_delete_cart(self):
        cart = Cart.objects.create(product=self.product_laptop,
                                   user=self.user,
                                   quantity=8,
                                   token=self.token)
        cart_id = cart.id

        self.assertEquals('product_laptop_test', cart.product.name)
        self.assertEquals('username_test', cart.user.username)
        self.assertEquals(8, cart.quantity)
        self.assertEquals(self.token, cart.token)

        cart.delete()
        self.assertRaises(Cart.DoesNotExist, Cart.objects.get, id=cart_id)


class CartApiTest(TestCase):
    def setUp(self) -> None:
        self.cart_url = '/api/carts'
        self.client = APIClient()
        self.category_tv = Category.objects.create(name='category_tv_test')
        self.category_laptop = Category.objects.create(name='category_laptop_test')
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

    def test_post_cart(self):
        payload_tv = {
            'product': self.product_tv.id,
            'quantity': 12
        }
        result_tv = self.client.post(f'{self.cart_url}/', payload_tv, **{"HTTP_AUTHORIZATION": f"Token {self.token}"})
        self.assertEquals(result_tv.status_code, status.HTTP_200_OK)
        self.assertEquals(result_tv.data['message'], 'success')

        payload_laptop = {
            'product': self.product_laptop.id,
            'quantity': 4
        }
        result_laptop = self.client.post(f'{self.cart_url}/', payload_laptop, **{"HTTP_AUTHORIZATION": f"Token {self.token}"})
        self.assertEquals(result_laptop.status_code, status.HTTP_200_OK)
        self.assertEquals(result_laptop.data['message'], 'success')

        cart_content = self.client.get(f'{self.cart_url}/', **{"HTTP_AUTHORIZATION": f"Token {self.token}"})
        self.assertEquals(cart_content.status_code, status.HTTP_200_OK)
        self.assertEquals(len(cart_content.data), 2)

    def test_delete_cart(self):
        payload_tv = {
            'product': self.product_tv.id,
            'quantity': 12
        }
        result_tv = self.client.post(f'{self.cart_url}/', payload_tv, **{"HTTP_AUTHORIZATION": f"Token {self.token}"})
        self.assertEquals(result_tv.status_code, status.HTTP_200_OK)
        self.assertEquals(result_tv.data['message'], 'success')

        payload_laptop = {
            'product': self.product_laptop.id,
            'quantity': 4
        }
        result_laptop = self.client.post(f'{self.cart_url}/', payload_laptop, **{"HTTP_AUTHORIZATION": f"Token {self.token}"})
        self.assertEquals(result_laptop.status_code, status.HTTP_200_OK)
        self.assertEquals(result_laptop.data['message'], 'success')

        get_cart_content = self.client.get(f'{self.cart_url}/', **{"HTTP_AUTHORIZATION": f"Token {self.token}"})
        self.assertEquals(get_cart_content.status_code, status.HTTP_200_OK)
        self.assertEquals(get_cart_content.data[1].get('product'), 'product_laptop_test')

        delete_laptop = self.client.delete(f'{self.cart_url}/', {'id': get_cart_content.data[1].get('id')}, **{"HTTP_AUTHORIZATION": f"Token {self.token}"})
        self.assertEquals(delete_laptop.status_code, status.HTTP_200_OK)
        self.assertEquals(delete_laptop.data['message'], 'Product was removed successfully')

        check_delete_laptop = self.client.delete(f'{self.cart_url}/', {'id': get_cart_content.data[1].get('id')}, **{"HTTP_AUTHORIZATION": f"Token {self.token}"})
        self.assertEquals(check_delete_laptop.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(check_delete_laptop.data['message'], 'Wrong cart id')

        cart_content = self.client.get(f'{self.cart_url}/', **{"HTTP_AUTHORIZATION": f"Token {self.token}"})
        self.assertEquals(cart_content.status_code, status.HTTP_200_OK)
        self.assertEquals(len(cart_content.data), 1)
