from django.urls import path
from . import views
from .models import Product

app_name = 'reviews'

urlpatterns = [
    path('<int:product_id>/', views.rate_product, name='rate_product'),
]
