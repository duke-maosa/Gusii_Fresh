# support/urls.py

from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('create/', views.create_ticket, name='create_ticket'),
    path('<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('<int:ticket_id>/reply/', views.reply_to_ticket, name='reply_to_ticket'),
    path('support/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
]
