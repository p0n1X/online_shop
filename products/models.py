from django.db import models
from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=256, blank=False, null=True)
    active = models.BooleanField(default=True)
    sku_number = models.IntegerField(default=0)
    description = models.CharField(max_length=2047, blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(to=Category, on_delete=models.DO_NOTHING, blank=False)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=False, null=True)

    def __str__(self):
        return self.name
