from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .supplier import SupplierController


class SupplierView(APIView):
    def get(self, request):
        supplier = SupplierController.get_all()
        return Response(data=supplier, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get('name')
        price = request.data.get('price')
        supplier = SupplierController.create_supplier(name, price)
        return Response(data={'message': f'The Supplier {supplier.name} was created successfully'}, status=status.HTTP_200_OK)

    def delete(self, request):
        id = request.data.get('id')
        try:
            SupplierController.delete_supplier(id)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_404_NOT_FOUND)
        return Response(data={'message': 'The Supplier was removed successfully'}, status=status.HTTP_200_OK)


class SingleSupplierView(APIView):
    def get(self, request, id):
        supplier = SupplierController.get_single_supplier(id)
        return Response(data=supplier, status=status.HTTP_200_OK)

    def put(self, request, id):
        name = request.data.get('name')
        price = request.data.get('price')
        try:
            supplier = SupplierController.update_supplier(name, price, id)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_404_NOT_FOUND)
        return Response(data=supplier, status=status.HTTP_200_OK)
