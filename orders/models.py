from django.db import models
from account.models import CustomUser  # Import CustomUser model
from products.models import Product  # Import Product model

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField('OrderItem', related_name='orders')  # Added related_name
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    is_completed = models.BooleanField(default=False)
    shipping_address = models.TextField(blank=True, null=True)
    tracking_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'Order #{self.id} - {self.user.username}'

    def calculate_total_cost(self):
        self.total_cost = sum(item.total_price for item in self.items.all())
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to the Product model
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f'{self.quantity} x {self.product}'
