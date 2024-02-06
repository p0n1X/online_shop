from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .cart import CartController


class CartView(APIView):
    def get(self, request):
        try:
            data = CartController.get_items(request.user)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_204_NO_CONTENT)

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        product_id = request.data.get('product')
        quantity = int(request.data.get('quantity'))
        try:
            CartController.add_item(product_id, quantity, request.user)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_204_NO_CONTENT)

        return Response(data={'message': 'success'}, status=status.HTTP_200_OK)

    def delete(self, request):
        id = request.data.get('id')
        try:
            CartController.remove_item(id)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_204_NO_CONTENT)
        return Response(data={'message': 'Product was removed successfully'}, status=status.HTTP_200_OK)


