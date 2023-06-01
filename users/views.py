from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
import logging


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serialized = UserSerializer(users, many=True)
        return Response(data=serialized.data, status=status.HTTP_200_OK)

    def post(self, request):
        username = request.data.get('username')
        first_name = request.data.get('firstname')
        last_name = request.data.get('lastname')
        address = request.data.get('address')
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.create(username=username,
                                   first_name=first_name,
                                   last_name=last_name,
                                   address=address,
                                   email=email,
                                   password=make_password(password))
        logging.info(f'The User {user.username} was created successfully')
        return Response(data={'message': 'success'}, status=status.HTTP_200_OK)


class SingleUserView(APIView):
    def get(self, request):
        try:
            user = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            logging.error('Invalid User ID')
            return Response(data={'error': 'Invalid User ID'}, status=status.HTTP_404_NOT_FOUND)

        serialized = UserSerializer(user, many=False)
        return Response(data=serialized.data, status=status.HTTP_200_OK)

    def put(self, request):
        id = request.data.get('id')
        username = request.data.get('username')
        first_name = request.data.get('firstname')
        last_name = request.data.get('lastname')
        email = request.data.get('email')
        address = request.data.get('address')

        try:
            user = User.objects.get(pk=id)
        except User.DoesNotExist:
            logging.error('Invalid User ID')
            return Response(data={'error': 'Invalid User ID'}, status=status.HTTP_404_NOT_FOUND)

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.address = address
        user.save()
        logging.info(f'The User {user.username} was updated successfully')
        return Response(data={'message': 'The User was updated successfully'}, status=status.HTTP_200_OK)


class UserLoginView(APIView):
    def get(self, request):
        try:
            Token.objects.get(user=request.user.id)
        except Token.DoesNotExist:
            logging.error('User is not login')
            return Response(data={'message': 'User is not login', 'login': False}, status=status.HTTP_404_NOT_FOUND)

        logging.info('User is login')
        return Response(data={'message': 'User is login', 'login': True}, status=status.HTTP_200_OK)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            logging.error('Invalid User')
            return Response(data={'message': 'Invalid User'}, status=status.HTTP_404_NOT_FOUND)

        if not check_password(password, user.password):
            logging.error('Invalid password')
            return Response(data={'message': 'Invalid password'}, status=status.HTTP_404_NOT_FOUND)

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
        return Response(data=response, status=status.HTTP_200_OK)


class UserLogoutView(APIView):
    def get(self, request):
        pass

    def delete(self, request):
        try:
            Token.objects.get(user=request.user.id).delete()
        except Token.DoesNotExist:
            return Response(data={'message': 'User is not login'}, status=status.HTTP_404_NOT_FOUND)
        logout(request)
        return Response(data={'message': 'User has successfully logout'}, status=status.HTTP_200_OK)
