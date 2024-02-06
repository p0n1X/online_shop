import logging
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout
from .models import User
from .serializers import UserSerializer


class UserController:

    @staticmethod
    def get_user_by_id(id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            logging.error('Invalid User ID')
            return None
        return user

    @staticmethod
    def get_users():
        users = User.objects.all()
        serialized = UserSerializer(users, many=True)
        return serialized.data

    @staticmethod
    def create_user(username, first_name, last_name, address, email, password):
        user = User.objects.create(username=username,
                                   first_name=first_name,
                                   last_name=last_name,
                                   address=address,
                                   email=email,
                                   password=make_password(password))
        logging.info(f'The User {user.username} was created successfully')

    @staticmethod
    def get_single_user(id):
        user = UserController.get_user_by_id(id)
        serialized = UserSerializer(user, many=False)

        return serialized.data

    @staticmethod
    def update_user(first_name, last_name, address, email, user_id):
        user = UserController.get_user_by_id(user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.address = address
        user.save()
        logging.info(f'The User {user.username} was updated successfully')

    @staticmethod
    def check_user(id):
        try:
            Token.objects.get(user=id)
        except Token.DoesNotExist:
            logging.error('User is not login')
            return ValueError('User is not login')

        logging.info('User is login')

    @staticmethod
    def login(request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            logging.error('Invalid User')
            return ValueError('Invalid User')

        if not check_password(password, user.password):
            logging.error('Invalid password')
            return ValueError('Invalid password')

        try:
            token = Token.objects.get(user=user)
            token.delete()
        except Token.DoesNotExist:
            pass
        finally:
            token = Token.objects.create(user=user)

        login(request, user)
        response = {}
        response['token'] = token.key

        logging.info(f'The User {user.username} was login successfully')

        return response

    @staticmethod
    def logout(request):
        try:
            Token.objects.get(user=request.user.id).delete()
        except Token.DoesNotExist:
            return ValueError('User is not login')
        logout(request)
