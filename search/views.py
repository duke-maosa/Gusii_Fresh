# search/views.py

from django.shortcuts import render
from products.models import Product
from accounts.models import CustomUser  # Import the CustomUser model from accounts app

def search(request):
    query = request.GET.get('q')
    if query:
        sellers = CustomUser.objects.filter(user_type='seller', username__icontains=query)
        products = Product.objects.filter(name__icontains=query) | Product.objects.filter(description__icontains=query)
        buyers = CustomUser.objects.filter(user_type='buyer', username__icontains=query)
        context = {
            'sellers': sellers,
            'products': products,
            'buyers': buyers,
            'query': query,
        }
    else:
        context = {}
    return render(request, 'search/search_results.html', context)
