import logging
from datetime import datetime
from .models import Product
from .serializers import ProductSerializer
from categories.category import CategoryController


class ProductController:

    @staticmethod
    def get_product_by_id(product_id):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            logging.error('Invalid Product ID')
            return ValueError('Invalid Product ID')
        return product

    @staticmethod
    def get_products():
        products = Product.objects.all().order_by('-id')
        serialized = ProductSerializer(products, many=True)
        return serialized.data

    @staticmethod
    def crete_product(name, sku_number, description, quantity, price, category_id):
        category = CategoryController.get_category_by_id(category_id)
        Product.objects.create(name=name,
                               active=True,
                               sku_number=sku_number,
                               description=description,
                               date=datetime.now(),
                               quantity=quantity,
                               category=category,
                               price=price)

        logging.info('The Product was created successfully')

    @staticmethod
    def delete_product(id):
        try:
            Product.objects.get(id=id).delete()
        except Product.DoesNotExist:
            logging.error('Wrong product id')
            return ValueError('Wrong product id')

        logging.info('The Product was removed successfully')

    @staticmethod
    def get_single_product(id):
        product = ProductController.get_product_by_id(id)
        serialized = ProductSerializer(product, many=False)
        return serialized.data

    @staticmethod
    def update_product(name, sku_number, description, quantity, price, category_id, product_id):
        product = ProductController.get_product_by_id(product_id)
        category = CategoryController.get_category_by_id(category_id)

        product.name = name
        product.sku_number = sku_number
        product.description = description
        product.quantity = quantity

        product.category = category
        product.price = price

        product.save()
        logging.info(f'The Product {product.name} was updated successfully')
        serialized = ProductSerializer(product, many=False)

        return serialized.data

    @staticmethod
    def get_all_products_from_category(category_id):
        try:
            products = Product.objects.filter(category__id=category_id)
        except Product.DoesNotExist:
            logging.error('Invalid Product ID')
            return ValueError('Invalid Product ID')

        serialized = ProductSerializer(products, many=True)

        return serialized.data