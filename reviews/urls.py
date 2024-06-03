from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('<int:product_id>/', views.product_reviews, name='product_reviews'),
]
