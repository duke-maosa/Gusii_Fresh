from django.urls import path
from . import views

urlpatterns = [
    path('enable-2fa/', views.enable_2fa, name='enable_2fa'),
]
