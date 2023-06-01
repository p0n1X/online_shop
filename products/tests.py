from django.test import TestCase
from .models import Product
from categories.models import Category
from rest_framework.test import APIClient
from rest_framework import status


class ProductTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='category_test')
        self.product = Product.objects.create(name='product_test',
                                              active=True,
                                              sku_number=4523532,
                                              description='product description',
                                              quantity=5,
                                              category=self.category,
                                              price=234.56)

    def test_get_product(self):
        product = Product.objects.get(name='product_test')
        self.assertEquals('product_test', product.name)
        self.assertTrue(product.active)
        self.assertEquals(4523532, product.sku_number)
        self.assertEquals(5, product.quantity)
        self.assertEquals('product description', product.description)
        self.assertEquals(self.category, product.category)
        self.assertEquals(234.56, float(product.price))

    def test_delete_product(self):
        check_product = Product.objects.filter(name='product_test')
        self.assertEquals(len(check_product), 1)

        Product.objects.get(name='product_test').delete()

        product = Product.objects.filter(name='product_test')
        self.assertEquals(len(product), 0)

    def test_post_product(self):
        product = Product.objects.create(name='product_create_test',
                                         active=True,
                                         sku_number=7656856,
                                         description='product create description',
                                         quantity=18,
                                         category=self.category,
                                         price=46.26)
        self.assertEquals('product_create_test', product.name)
        self.assertTrue(product.active)
        self.assertEquals(7656856, product.sku_number)
        self.assertEquals(18, product.quantity)
        self.assertEquals('product create description', product.description)
        self.assertEquals(self.category, product.category)
        self.assertEquals(46.26, float(product.price))

    def test_update_product(self):
        self.product.name = 'product_update_test'
        self.product.description = 'product update description'
        self.product.quantity = 86
        self.product.save()

        self.assertEquals('product_update_test', self.product.name)
        self.assertEquals('product update description', self.product.description)
        self.assertEquals(86, self.product.quantity)
        self.assertEquals(234.56, float(self.product.price))
        self.assertEquals(self.category, self.product.category)


class ProductApiTest(TestCase):
    def setUp(self):
        self.product_url = '/api/products'
        self.client = APIClient()
        self.category = Category.objects.create(name='category_test')
        self.product = Product.objects.create(name='product_test',
                                              active=True,
                                              sku_number=4523532,
                                              description='product description',
                                              quantity=5,
                                              category=self.category,
                                              price=234.56)

    def test_create_product(self):
        payload = {
            'name': "product_create_test",
            'active': True,
            'sku_number': 7656856,
            'description': 'product create description',
            'quantity': 18,
            'category': self.category.id,
            'price': 46.26
        }
        result = self.client.post(f'{self.product_url}/', payload)
        self.assertEquals(result.status_code, status.HTTP_200_OK)

    def test_delete_product(self):
        payload = {
            'id': self.product.id
        }
        result = self.client.delete(f'{self.product_url}/', payload)
        self.assertEquals(result.status_code, status.HTTP_200_OK)
        self.assertEquals(result.data['message'], 'The Product was removed successfully')

    def test_get_product(self):
        result = self.client.get(f'{self.product_url}/')
        self.assertEquals(result.status_code, status.HTTP_200_OK)
        self.assertEquals(len(result.data), 1)
        self.assertEquals(result.data[0]['name'], 'product_test')
        self.assertEquals(result.data[0]['description'], 'product description')
        self.assertEquals(result.data[0]['sku_number'], 4523532)
        self.assertEquals(result.data[0]['category'], self.category.name)

    def test_update_product(self):
        payload = {
            'name': 'product_update_test',
            'sku_number': 7567567,
            'description': 'product update description',
            'quantity': 45,
            'category': self.category.id,
            'price': 42.34
        }

        result = self.client.put(f'{self.product_url}/{self.product.id}', payload)
        self.assertEquals(result.status_code, status.HTTP_200_OK)
        self.assertEquals(result.data['name'], 'product_update_test')
