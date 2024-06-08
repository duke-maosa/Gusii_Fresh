from django.db import models
from django.conf import settings
from products.models import Product  

class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f'{self.product.name} (x{self.quantity})'

    def increase_quantity(self, quantity_increment=1):
        """
        Increase the quantity of the cart item by a specified increment.
        """
        self.quantity += quantity_increment
        self.save()

    def decrease_quantity(self, quantity_decrement=1):
        """
        Decrease the quantity of the cart item by a specified decrement.
        """
        if self.quantity > quantity_decrement:
            self.quantity -= quantity_decrement
            self.save()
        else:
            self.delete()

    @property
    def subtotal(self):
        """
        Calculate the subtotal for the cart item (price * quantity).
        """
        return self.quantity * self.product.price
