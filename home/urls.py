from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name= 'about_us'),
    path('contact/', views.contact_us, name= 'contact_us')
]
