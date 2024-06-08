from django.db import models
from account.models import CustomUser

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    link = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    priority = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.message}'
