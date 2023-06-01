from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import status
import logging


class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serialized = CategorySerializer(categories, many=True)
        return Response(data=serialized.data, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get('name')
        category = Category.objects.create(name=name,)
        logging.info(f'Category {category.name} was created successfully')
        return Response(data={'message': 'success'}, status=status.HTTP_200_OK)

    def delete(self, request):
        id = request.data.get('id')
        try:
            Category.objects.get(id=id).delete()
        except Category.DoesNotExist:
            logging.error('Wrong category id')
            return Response(data={'message': 'Wrong category id'}, status=status.HTTP_204_NO_CONTENT)

        logging.info('Category was removed successfully')
        return Response(data={'message': 'Category was removed successfully'}, status=status.HTTP_200_OK)


class SingleCategoryView(APIView):
    def get(self, request, id):
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            logging.error('Invalid Category ID')
            return Response(data={'error': 'Invalid Category ID'}, status=status.HTTP_404_NOT_FOUND)

        serialized = CategorySerializer(category, many=False)
        return Response(data=serialized.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        name = request.data.get('name')

        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            logging.error('Invalid Category ID')
            return Response(data={'error': 'Invalid Category ID'}, status=status.HTTP_404_NOT_FOUND)

        category.name = name
        category.save()
        logging.info(f'The Category {category.name} was updated successfully')
        serialized = CategorySerializer(category, many=False)
        return Response(data=serialized.data, status=status.HTTP_200_OK)
