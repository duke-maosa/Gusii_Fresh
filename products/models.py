import uuid
from django.db import models
from account.models import CustomUser
from django.core.exceptions import ValidationError

def validate_rating(value):
    if value < 0 or value > 5:
        raise ValidationError('Rating must be between 0 and 5.')

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('category1', 'Category 1'),
        ('category2', 'Category 2'),
        ('category3', 'Category 3'),
        # Add more choices as needed
    ]

    DEFAULT_CATEGORY = 'category1'

    unique_identifier = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity = models.PositiveIntegerField()
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='seller_products')
    ratings = models.FloatField(default=0, validators=[validate_rating])
    total_ratings = models.PositiveIntegerField(default=0)
    sales_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product_images/', default='homepic.jpeg')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=DEFAULT_CATEGORY)

    def __str__(self):
        return self.name

    def average_rating(self):
        if self.total_ratings > 0:
            return round(self.ratings / self.total_ratings, 2)
        else:
            return 0

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    rating = models.PositiveIntegerField(validators=[validate_rating])
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.product.name} by {self.reviewer.username}'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/product_images/', default='homepic.jpeg')

    def __str__(self):
        return f'Image for {self.product.name}'