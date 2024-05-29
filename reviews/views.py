from django.shortcuts import render, get_object_or_404
from .models import Review
from products.models import Product

def product_reviews(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)
    return render(request, 'reviews/product_reviews.html', {'product': product, 'reviews': reviews})
