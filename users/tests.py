from django.test import TestCase, RequestFactory
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.test import APIClient
from rest_framework import status


class UserTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='username_test',
                                        first_name='John',
                                        last_name='Doe',
                                        address='Plovdiv',
                                        email='john.doe@jonhmail.com',
                                        password=make_password('test_pass'))

    def test_get_user(self):
        user_obj = User.objects.get(username='username_test')
        self.assertEquals('username_test', user_obj.username)

    def test_post_user(self):
        user_obj = User.objects.create(username='username_create_test',
                                       first_name='John',
                                       last_name='Doe',
                                       address='Plovdiv',
                                       email='john.doe@jonhmail.com',
                                       password=make_password('test_pass'))

        self.assertEquals('username_create_test', user_obj.username)
        self.assertEquals('John', user_obj.first_name)
        self.assertEquals('Doe', user_obj.last_name)
        self.assertEquals('Plovdiv', user_obj.address)
        self.assertEquals('john.doe@jonhmail.com', user_obj.email)
        self.assertTrue(check_password('test_pass', user_obj.password))

    def test_update_user(self):
        self.user.username = 'username_update_test'
        self.user.first_name = 'Jane'
        self.user.email = 'jane.doe@janemail.com'
        self.user.password = make_password('test_update_pass')
        self.user.save()

        self.assertEquals('username_update_test', self.user.username)
        self.assertEquals('Jane', self.user.first_name)
        self.assertEquals('Doe', self.user.last_name)
        self.assertEquals('Plovdiv', self.user.address)
        self.assertEquals('jane.doe@janemail.com', self.user.email)
        self.assertTrue(check_password('test_update_pass', self.user.password))


class UserApiTest(TestCase):
    def setUp(self) -> None:
        self.user_url = '/api/users'
        self.client = APIClient()
        self.user = User.objects.create(username='username_test',
                                        first_name='John',
                                        last_name='Doe',
                                        address='Plovdiv',
                                        email='john.doe@jonhmail.com',
                                        password=make_password('test_pass'))

    def test_get_user(self):
        result = self.client.get(f'{self.user_url}/')
        self.assertEquals(result.status_code, status.HTTP_200_OK)
        self.assertEquals(len(result.data), 1)
        self.assertEquals(result.data[0]['username'], 'username_test')
        self.assertEquals(result.data[0]['first_name'], 'John')
        self.assertEquals(result.data[0]['email'], 'john.doe@jonhmail.com')
        self.assertTrue(check_password('test_pass', result.data[0]['password']))

    def test_create_user(self):
        payload = {
            'username': 'username_create_test',
            'first_name': 'John',
            'last_name': 'Doe',
            'address': 'Plovdiv',
            'email': 'john.doe@jonhmail.com',
            'password': make_password('test_pass')
        }
        result = self.client.post(f'{self.user_url}/', payload)
        self.assertEquals(result.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        payload = {
            'id': self.user.id,
            'username': 'username_update_test',
            'first_name': 'Jane',
            'email': 'jane.doe@janemail.com',
            'password': make_password('test_update_pass')
        }
        result = self.client.put(f'{self.user_url}/info', payload)
        self.assertEquals(result.status_code, status.HTTP_200_OK)
        self.assertEquals(result.data['message'], 'The User was updated successfully')

    def test_user_login(self):
        check_logout = self.client.get(f'{self.user_url}/login')
        self.assertEquals(check_logout.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(check_logout.data, 'User is not login')

        payload = {
            'username': 'username_test',
            'password': 'test_pass'
        }
        result = self.client.post(f'{self.user_url}/login', payload)
        self.assertEquals(result.status_code, status.HTTP_200_OK)

        check_login = self.client.get(f'{self.user_url}/login', **{"HTTP_AUTHORIZATION": f"Token {result.data['token']}"})
        self.assertEquals(check_login.status_code, status.HTTP_200_OK)
        self.assertTrue(check_login.data['login'])

    def test_user_logout(self):
        payload = {
            'username': 'username_test',
            'password': 'test_pass'
        }
        result = self.client.post(f'{self.user_url}/login', payload)
        self.assertEquals(result.status_code, status.HTTP_200_OK)

        check_login = self.client.get(f'{self.user_url}/login', **{"HTTP_AUTHORIZATION": f"Token {result.data['token']}"})
        self.assertEquals(check_login.status_code, status.HTTP_200_OK)
        self.assertTrue(check_login.data['login'])

        check_logout = self.client.delete(f'{self.user_url}/logout', **{"HTTP_AUTHORIZATION": f"Token {result.data['token']}"})
        self.assertEquals(check_logout.status_code, status.HTTP_200_OK)
        self.assertEquals(check_logout.data['message'], 'User has successfully logout')

        check_login_again = self.client.delete(f'{self.user_url}/logout', **{"HTTP_AUTHORIZATION": f"Token {result.data['token']}"})
        self.assertEquals(check_login_again.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEquals(check_login_again.headers.get('WWW-Authenticate'), 'Token')



