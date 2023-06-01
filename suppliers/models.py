from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=True)

    def __str__(self):
        return self.name
