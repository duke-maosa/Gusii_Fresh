from django.urls import path
from . import views
from cart import views as cart_views  # Import views module from the cart app

app_name = 'products'

urlpatterns = [
     path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('create/', views.create_product, name='create_product'),
    path('<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('cart/', cart_views.add_to_cart, name='add_to_cart'),  # Use add_to_cart from cart app
]
