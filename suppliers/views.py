from rest_framework.views import APIView
from .models import Supplier
from .serializers import SupplierSerializer
from rest_framework.response import Response
from rest_framework import status
import logging


class SupplierView(APIView):
    def get(self, request):
        suppliers = Supplier.objects.all()
        serialized = SupplierSerializer(suppliers, many=True)
        return Response(data=serialized.data, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get('name')
        price = request.data.get('price')

        supplier = Supplier.objects.create(name=name, price=price)
        logging.info(f'The Supplier {supplier.name} was created successfully')
        return Response(data={'message': f'The Supplier {supplier.name} was created successfully'}, status=status.HTTP_200_OK)

    def delete(self, request):
        id = request.data.get('id')
        try:
            Supplier.objects.get(id=id).delete()
        except Supplier.DoesNotExist:
            logging.error('Wrong supplier id')
            return Response(data={'message': 'Wrong supplier id'}, status=status.HTTP_204_NO_CONTENT)

        logging.info('The Supplier was removed successfully')
        return Response(data={'message': 'The Supplier was removed successfully'}, status=status.HTTP_200_OK)


class SingleSupplierView(APIView):
    def get(self, request, id):
        try:
            supplier = Supplier.objects.get(id=id)
        except Supplier.DoesNotExist:
            logging.error('Invalid Supplier ID')
            return Response(data={'error': 'Invalid Supplier ID'}, status=status.HTTP_404_NOT_FOUND)

        serialized = SupplierSerializer(supplier, many=False)
        return Response(data=serialized.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        name = request.data.get('name')
        price = request.data.get('price')

        try:
            supplier = Supplier.objects.get(id=id)
        except Supplier.DoesNotExist:
            logging.error('Invalid Supplier ID')
            return Response(data={'error': 'Invalid Supplier ID'}, status=status.HTTP_404_NOT_FOUND)

        supplier.name = name
        supplier.price = price
        supplier.save()
        logging.info(f'The Supplier {supplier.name} was updated successfully')
        serialized = SupplierSerializer(supplier, many=False)
        return Response(data=serialized.data, status=status.HTTP_200_OK)
