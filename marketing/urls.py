from django.urls import path
from . import views



app_name = 'marketing'

urlpatterns = [
    path('newsletter/signup/', views.newsletter_signup, name='newsletter_signup'),
    # Add more URLs for other marketing functionalities
]
