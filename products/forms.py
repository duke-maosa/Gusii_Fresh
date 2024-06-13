from django import forms
from .models import Product

app_use = 'products'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'available_quantity','price', 'image']
