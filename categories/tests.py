from django.test import TestCase
from .models import Category
from rest_framework.test import APIClient
from rest_framework import status


class CategoryTest(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name='category_test')

    def test_get_category(self):
        category = Category.objects.get(name='category_test')
        self.assertEquals('category_test', category.name)

    def test_delete_category(self):
        check_category = Category.objects.filter(name='category_test')
        self.assertEquals(len(check_category), 1)

        Category.objects.get(name='category_test').delete()

        category = Category.objects.filter(name='category_test')
        self.assertEquals(len(category), 0)

    def test_post_category(self):
        category = Category.objects.create(name='category_create_test')
        self.assertEquals('category_create_test', category.name)

    def test_update_category(self):
        category = Category.objects.get(name='category_test')
        category.name = 'category_update_test'
        category.save()
        self.assertEquals('category_update_test', category.name)


class CategoryApiTest(TestCase):
    def setUp(self) -> None:
        self.category_url = '/api/categories'
        self.client = APIClient()
        self.category = Category.objects.create(name='category_test')

    def test_create_category(self):
        payload = {
            'name': "category_create_test"
        }
        result = self.client.post(f'{self.category_url}/', payload)
        self.assertEquals(result.status_code, status.HTTP_200_OK)

    def test_delete_category(self):
        payload = {
            'id': self.category.id
        }
        result = self.client.delete(f'{self.category_url}/', payload)
        self.assertEquals(result.status_code, status.HTTP_200_OK)
        self.assertEquals(result.data['message'], 'Category was removed successfully')

    def test_get_category(self):
        result = self.client.get(f'{self.category_url}/')
        self.assertEquals(result.status_code, status.HTTP_200_OK)
        self.assertEquals(len(result.data), 1)
        self.assertEquals(result.data[0]['name'], 'category_test')

    def test_update_category(self):
        payload = {
            'name': 'category_update_test'
        }
        result = self.client.put(f'{self.category_url}/{self.category.id}', payload)
        self.assertEquals(result.status_code, status.HTTP_200_OK)
        self.assertEquals(result.data['name'], 'category_update_test')
