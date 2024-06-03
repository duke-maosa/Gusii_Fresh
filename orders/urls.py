from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('order_processing/', views.order_processing, name='order_processing'),
    path('order_details/<int:order_id>/', views.order_details, name='order_details'),
    path('order_tracking/<int:order_id>/', views.order_tracking, name='order_tracking'),
    path('cancel_order/<int:order_id>/', views.cancel_order, name='cancel_order'),
]
