from django.db import models
from products.models import Product
from users.models import User
from suppliers.models import Supplier


class Order(models.Model):
    date = models.DateField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=15, decimal_places=2, blank=False, null=True)
    user = models.ForeignKey(
        to=User,
        blank=False,
        null=True,
        on_delete=models.DO_NOTHING
    )
    supplier = models.ForeignKey(to=Supplier, on_delete=models.DO_NOTHING, blank=False, null=True)

    def __str__(self):
        return f'Order Number: #{self.id}'


class OrderDetail(models.Model):
    order_number = models.ForeignKey(to=Order, blank=False, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, blank=False, null=False, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=False, null=True)

    def __str__(self):
        return f'Order Number: #{self.order_number.id} Product {self.product.name}'
