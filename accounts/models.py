from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    rated_by = models.ManyToManyField('self', symmetrical=False, through='CustomUserRating', related_name='received_ratings', blank=True)
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='custom_user_set')

    def __str__(self):
        return self.username

class CustomUserRating(models.Model):
    user = models.ForeignKey(CustomUser, related_name='given_ratings', on_delete=models.CASCADE)
    rated_by = models.ForeignKey(CustomUser, related_name='received_ratings_as_rated_by', on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        unique_together = ('user', 'rated_by')
