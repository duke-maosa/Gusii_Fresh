from django.contrib import admin
from .models import CustomUserInteraction, SalesData


# Register your models here.
admin.site.register(CustomUserInteraction)
admin.site.register(SalesData)