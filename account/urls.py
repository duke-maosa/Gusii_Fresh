from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.profile, name='profile'),
    path('rate/<int:user_id>/', views.rate_user, name='rate_user'),
]
