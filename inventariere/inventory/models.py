from django.db import models

from categories.models import Category


class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.category})"
