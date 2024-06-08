from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    rating = models.FloatField(default=0.0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='custom_user_set')

    def __str__(self):
        return self.username

class CustomUserRating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='given_ratings')
    rated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_ratings_as_rated_by')
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # Changed to FloatField

    class Meta:
        unique_together = ('user', 'rated_by')

