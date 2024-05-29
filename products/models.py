from django.db import models
from accounts.models import CustomUser  # Import CustomUser model from the accounts app

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity = models.PositiveIntegerField()
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Use CustomUser model here
    ratings = models.FloatField(default=0)
    total_ratings = models.PositiveIntegerField(default=0)
    sales_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def average_rating(self):
        if self.total_ratings > 0:
            return self.ratings / self.total_ratings
        else:
            return 0

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f'Image for {self.product.name}'
