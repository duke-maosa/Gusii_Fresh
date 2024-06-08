from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.notifications_list, name='notifications_list'),
    path('mark_as_read/<int:notification_id>/', views.mark_as_read, name='mark_as_read'),
    path('mark_all_as_read/', views.mark_all_as_read, name='mark_all_as_read'),
    path('delete_notification/<int:notification_id>/', views.delete_notification, name='delete_notification'),
    path('delete_all_notifications/', views.delete_all_notifications, name='delete_all_notifications'),
]
