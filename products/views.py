from rest_framework.views import APIView
from .models import Product
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from categories.models import Category
from datetime import datetime
import logging


class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all().order_by('-id')
        serialized = ProductSerializer(products, many=True)
        return Response(data=serialized.data, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get('name')
        sku_number = request.data.get('sku_number')
        description = request.data.get('description')
        quantity = request.data.get('quantity')
        category_id = request.data.get('category')
        price = request.data.get('price')

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            logging.error('Invalid Category ID')
            return Response(data={'error': 'Invalid Category ID'}, status=status.HTTP_404_NOT_FOUND)

        Product.objects.create(name=name,
                               active=True,
                               sku_number=sku_number,
                               description=description,
                               date=datetime.now(),
                               quantity=quantity,
                               category=category,
                               price=price)

        logging.info('The Product was created successfully')
        return Response(data={'message': 'The Product was created successfully'}, status=status.HTTP_200_OK)

    def delete(self, request):
        id = request.data.get('id')
        try:
            Product.objects.get(id=id).delete()
        except Product.DoesNotExist:
            logging.error('Wrong product id')
            return Response(data={'message': 'Wrong product id'}, status=status.HTTP_204_NO_CONTENT)

        logging.info('The Product was removed successfully')
        return Response(data={'message': 'The Product was removed successfully'}, status=status.HTTP_200_OK)


class SingleProductView(APIView):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            logging.error('Invalid Product ID')
            return Response(data={'error': 'Invalid Product ID'}, status=status.HTTP_404_NOT_FOUND)
        serialized = ProductSerializer(product, many=False)
        return Response(data=serialized.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        name = request.data.get('name')
        sku_number = request.data.get('sku_number')
        description = request.data.get('description')
        quantity = request.data.get('quantity')
        category_id = request.data.get('category')
        price = request.data.get('price')
        try:
            product = Product.objects.get(pk=id)
        except Product.DoesNotExist:
            logging.error('Invalid Product ID')
            return Response(data={'error': 'Invalid Product ID'}, status=status.HTTP_404_NOT_FOUND)

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            logging.error('Invalid Category ID')
            return Response(data={'error': 'Invalid Category ID'}, status=status.HTTP_404_NOT_FOUND)

        product.name = name
        product.sku_number = sku_number
        product.description = description
        product.quantity = quantity

        product.category = category
        product.price = price

        product.save()
        logging.info(f'The Product {product.name} was updated successfully')
        serialized = ProductSerializer(product, many=False)
        return Response(data=serialized.data, status=status.HTTP_200_OK)


class ProductCategoryView(APIView):
    def get(self, request, id):
        try:
            products = Product.objects.filter(category__id=id)
        except Product.DoesNotExist:
            logging.error('Invalid Product ID')
            return Response(data={'error': 'Invalid Product ID'}, status=status.HTTP_404_NOT_FOUND)

        serialized = ProductSerializer(products, many=True)
        return Response(data=serialized.data, status=status.HTTP_200_OK)
