import logging
from .models import Supplier
from .serializers import SupplierSerializer


class SupplierController:
    @staticmethod
    def get_suppliers_by_id(id):
        try:
            supplier = Supplier.objects.get(id=id)
        except Supplier.DoesNotExist:
            logging.error('Invalid supplier id')
            return ValueError('Invalid supplier id')
        return supplier

    @staticmethod
    def get_all():
        suppliers = Supplier.objects.all()
        serialized = SupplierSerializer(suppliers, many=True)
        return serialized.data

    @staticmethod
    def create_supplier(name, price):
        supplier = Supplier.objects.create(name=name, price=price)
        logging.info(f'The Supplier {supplier.name} was created successfully')
        return supplier

    @staticmethod
    def delete_supplier(id):
        try:
            Supplier.objects.get(id=id).delete()
        except Supplier.DoesNotExist:
            logging.error('Invalid supplier id')
            return ValueError('Invalid supplier id')

        logging.info('The Supplier was removed successfully')

    @staticmethod
    def get_single_supplier(id):
        supplier = SupplierController.get_suppliers_by_id(id)
        serialized = SupplierSerializer(supplier, many=False)
        return serialized.data

    @staticmethod
    def update_supplier(name, price, supplier_id):
        supplier = SupplierController.get_suppliers_by_id(supplier_id)
        supplier.name = name
        supplier.price = price
        supplier.save()
        logging.info(f'The Supplier {supplier.name} was updated successfully')
        serialized = SupplierSerializer(supplier, many=False)

        return serialized.data
