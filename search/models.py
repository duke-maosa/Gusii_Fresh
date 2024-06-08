from django.db import models
from account.models import CustomUser

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='search_seller_products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
