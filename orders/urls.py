from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.order_processing, {'action': 'checkout'}, name='checkout'),
    path('order_details/<int:order_id>/', views.order_processing, {'action': 'details'}, name='order_details'),
    path('order_tracking/<int:order_id>/', views.order_processing, {'action': 'tracking'}, name='order_tracking'),
    path('cancel_order/<int:order_id>/', views.order_processing, {'action': 'cancel'}, name='cancel_order'),
]
