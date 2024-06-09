from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('create/', views.create_product, name='create_product'),
    path('<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('<int:product_id>/delete/', views.delete_product, name='delete_product'),
]
