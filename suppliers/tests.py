from django.test import TestCase
from .models import Supplier
from rest_framework.test import APIClient
from rest_framework import status


class SupplierTest(TestCase):
    def setUp(self) -> None:
        self.supplier = Supplier.objects.create(name='supplier_test')

    def test_get_supplier(self):
        supplier = Supplier.objects.get(name='supplier_test')
        self.assertEquals('supplier_test', supplier.name)

    def test_delete_supplier(self):
        check_supplier = Supplier.objects.filter(name='supplier_test')
        self.assertEquals(len(check_supplier), 1)

        Supplier.objects.get(name='supplier_test').delete()

        supplier = Supplier.objects.filter(name='supplier_test')
        self.assertEquals(len(supplier), 0)

    def test_post_supplier(self):
        supplier = Supplier.objects.create(name='supplier_create_test')
        self.assertEquals('supplier_create_test', supplier.name)

    def test_update_supplier(self):
        supplier = Supplier.objects.get(name='supplier_test')
        supplier.name = 'supplier_update_test'
        supplier.save()
        self.assertEquals('supplier_update_test', supplier.name)


class SupplierApiTest(TestCase):
    def setUp(self) -> None:
        self.supplier_url = '/api/suppliers'
        self.client = APIClient()
        self.supplier = Supplier.objects.create(name='supplier_test')

    def test_create_supplier(self):
        payload = {
            'name': "supplier_create_test"
        }
        result = self.client.post(f'{self.supplier_url}/', payload)
        self.assertEquals(result.status_code, status.HTTP_200_OK)

    def test_delete_supplier(self):
        payload = {
            'id': self.supplier.id
        }
        result = self.client.delete(f'{self.supplier_url}/', payload)
        self.assertEquals(result.status_code, status.HTTP_200_OK)
        self.assertEquals(result.data['message'], 'The Supplier was removed successfully')

    def test_get_supplier(self):
        result = self.client.get(f'{self.supplier_url}/')
        self.assertEquals(result.status_code, status.HTTP_200_OK)
        self.assertEquals(len(result.data), 1)
        self.assertEquals(result.data[0]['name'], 'supplier_test')

    def test_update_supplier(self):
        payload = {
            'name': 'supplier_update_test'
        }
        result = self.client.put(f'{self.supplier_url}/{self.supplier.id}', payload)
        self.assertEquals(result.status_code, status.HTTP_200_OK)
        self.assertEquals(result.data['name'], 'supplier_update_test')
