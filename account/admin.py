from django.contrib import admin
from .models import CustomUser, CustomUserRating
# Register your models here.
admin.site.register(CustomUserRating)
admin.site.register(CustomUser)