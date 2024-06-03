from django.urls import path
from . import views



app_name = 'payments'

urlpatterns = [
    path('initiate_payment/', views.initiate_payment, name='initiate_payment'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_failure/', views.payment_failure, name='payment_failure'),
]
