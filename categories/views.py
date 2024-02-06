from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .category import CategoryController


class CategoryView(APIView):
    def get(self, request):
        categories = CategoryController.get_categories()
        return Response(data=categories, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get('name')
        CategoryController.add_category(name)
        return Response(data={'message': 'Category was created successfully'}, status=status.HTTP_200_OK)

    def delete(self, request):
        id = request.data.get('id')
        try:
            CategoryController.delete_category(id)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_404_NOT_FOUND)
        return Response(data={'message': 'Category was removed successfully'}, status=status.HTTP_200_OK)


class SingleCategoryView(APIView):
    def get(self, request, id):
        try:
            category = CategoryController.get_single_category(id)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_404_NOT_FOUND)
        return Response(data=category, status=status.HTTP_200_OK)

    def put(self, request, id):
        name = request.data.get('name')
        try:
            category = CategoryController.update_category(id, name)
        except ValueError as error:
            return Response(data=str(error), status=status.HTTP_404_NOT_FOUND)

        return Response(data=category, status=status.HTTP_200_OK)
