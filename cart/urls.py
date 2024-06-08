from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('checkout/', views.view_cart, name='checkout'),  # Changed the name to 'checkout'
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:cart_item_id>/', views.update_cart, name='update_cart'),
]
