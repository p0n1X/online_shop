from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .user import UserController


class UserView(APIView):
    def get(self, request):
        users = UserController.get_users()
        return Response(data=users, status=status.HTTP_200_OK)

    def post(self, request):
        username = request.data.get('username')
        first_name = request.data.get('firstname')
        last_name = request.data.get('lastname')
        address = request.data.get('address')
        email = request.data.get('email')
        password = request.data.get('password')

        UserController.create_user(username, first_name, last_name, address, email, password)
        return Response(data={'message': f'The User {username} was created successfully'}, status=status.HTTP_200_OK)


class SingleUserView(APIView):
    def get(self, request):
        try:
            user = UserController.get_single_user(request.user.id)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_404_NOT_FOUND)
        return Response(data=user, status=status.HTTP_200_OK)

    def put(self, request):
        id = request.data.get('id')
        first_name = request.data.get('firstname')
        last_name = request.data.get('lastname')
        email = request.data.get('email')
        address = request.data.get('address')
        try:
            UserController.update_user(first_name, last_name, address, email, id)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_404_NOT_FOUND)
        return Response(data={'message': 'The User was updated successfully'}, status=status.HTTP_200_OK)


class UserLoginView(APIView):
    def get(self, request):
        try:
            UserController.check_user(request.user.id)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_404_NOT_FOUND)
        return Response(data={'message': 'User is login', 'login': True}, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            response = UserController.login(request)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_404_NOT_FOUND)
        return Response(data=response, status=status.HTTP_200_OK)


class UserLogoutView(APIView):
    def get(self, request):
        pass

    def delete(self, request):
        try:
            UserController.logout(request)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_404_NOT_FOUND)
        return Response(data={'message': 'User has successfully logout'}, status=status.HTTP_200_OK)
