# products/views.py
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product

@login_required
def rate_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    rating = int(request.POST.get('rating'))
    if rating < 1 or rating > 5:
        messages.error(request, 'Invalid rating. Please rate between 1 and 5.')
    else:
        product.total_ratings += 1
        product.ratings += rating
        product.save()
        messages.success(request, 'Thanks for rating the product!')
    return redirect('products:product_detail', product_id=product.id)
