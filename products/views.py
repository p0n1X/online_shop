from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .product import ProductController


class ProductView(APIView):
    def get(self, request):
        products = ProductController.get_products()
        return Response(data=products, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get('name')
        sku_number = request.data.get('sku_number')
        description = request.data.get('description')
        quantity = request.data.get('quantity')
        category_id = request.data.get('category')
        price = request.data.get('price')
        try:
            ProductController.crete_product(name, sku_number, description, quantity, price, category_id)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_404_NOT_FOUND)
        return Response(data={'message': 'The Product was created successfully'}, status=status.HTTP_200_OK)

    def delete(self, request):
        id = request.data.get('id')
        try:
            ProductController.delete_product(id)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_404_NOT_FOUND)
        return Response(data={'message': 'The Product was removed successfully'}, status=status.HTTP_200_OK)


class SingleProductView(APIView):
    def get(self, request, id):
        try:
            product = ProductController.get_single_product(id)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_404_NOT_FOUND)
        return Response(data=product, status=status.HTTP_200_OK)

    def put(self, request, id):
        name = request.data.get('name')
        sku_number = request.data.get('sku_number')
        description = request.data.get('description')
        quantity = request.data.get('quantity')
        category_id = request.data.get('category')
        price = request.data.get('price')
        try:
            product = ProductController.update_product(name, sku_number, description, quantity, price, category_id, id)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_404_NOT_FOUND)

        return Response(data=product, status=status.HTTP_200_OK)


class ProductCategoryView(APIView):
    def get(self, request, id):
        try:
            products = ProductController.get_all_products_from_category(id)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_404_NOT_FOUND)
        return Response(data=products, status=status.HTTP_200_OK)
