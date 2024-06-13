from django.urls import path
from . import views
from cart.views import add_to_cart  # Import the add_to_cart view from the cart app

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),  # URL for listing all products
    path('<int:product_id>/', views.product_detail, name='product_detail'),  # URL for a specific product's details
    path('create/', views.create_product, name='create_product'),  # URL for creating a new product
    path('<int:product_id>/edit/', views.edit_product, name='edit_product'),  # URL for editing a product
    path('<int:product_id>/delete/', views.delete_product, name='delete_product'),  # URL for deleting a product
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),  # URL for adding a product to the cart
]
