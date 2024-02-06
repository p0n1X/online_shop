import logging
from .models import Category
from .serializers import CategorySerializer


class CategoryController:

    @staticmethod
    def get_category_by_id(id):
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            logging.error('Invalid Category ID')
            raise ValueError('Invalid Category ID')
        return category

    @staticmethod
    def get_categories():
        categories = Category.objects.all()
        serialized = CategorySerializer(categories, many=True)
        return serialized.data

    @staticmethod
    def add_category(name):
        category = Category.objects.create(name=name)
        logging.info(f'Category {category.name} was created successfully')

    @staticmethod
    def delete_category(id):
        try:
            Category.objects.get(id=id).delete()
        except Category.DoesNotExist:
            logging.error('Wrong category id')
            raise ValueError('Wrong category id')

        logging.info('Category was removed successfully')

    @staticmethod
    def get_single_category(id):
        category = CategoryController.get_category_by_id(id)
        serialized = CategorySerializer(category, many=False)

        return serialized.data

    @staticmethod
    def update_category(id, name):
        category = CategoryController.get_category_by_id(id)
        category.name = name
        category.save()
        logging.info(f'The Category {category.name} was updated successfully')
        serialized = CategorySerializer(category, many=False)

        return serialized.data
