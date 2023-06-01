from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
