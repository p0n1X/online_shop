from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .order import OrderController


class OrderView(APIView):
    def get(self, request):
        try:
            orders = OrderController.get_orders(request.user)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_204_NO_CONTENT)
        return Response(data=orders, status=status.HTTP_200_OK)

    def post(self, request):
        token = request.data.get('token', None)
        supplier_id = request.data.get('supplier', None)
        try:
            OrderController.create_order(token, supplier_id)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_404_NOT_FOUND)

        return Response(data={'message': 'The Order was created successfully'}, status=status.HTTP_200_OK)


class SingleOrderView(APIView):
    def get(self, request, id):
        try:
            order = OrderController.get_order(id)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_404_NOT_FOUND)
        return Response(data=order, status=status.HTTP_200_OK)
