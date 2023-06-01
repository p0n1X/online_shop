from django.db import models
from products.models import Product
from users.models import User


class Cart(models.Model):
    product = models.ForeignKey(
        to=Product,
        blank=False,
        null=True,
        on_delete=models.DO_NOTHING
    )
    user = models.ForeignKey(
        to=User,
        blank=False,
        null=True,
        on_delete=models.DO_NOTHING
    )
    quantity = models.IntegerField(default=0)
    token = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f'Shopping card number: {self.id}'
