from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
from .forms import ReviewForm

@login_required
def rate_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            if 1 <= rating <= 5:
                product.total_ratings += 1
                product.ratings += rating
                product.save()
                messages.success(request, 'Thanks for rating the product!')
            else:
                messages.error(request, 'Invalid rating. Please rate between 1 and 5.')
        else:
            messages.error(request, 'Invalid rating form submission.')
    else:
        form = ReviewForm()

    return redirect(request.POST.get('next', 'products:product_detail', args=[product_id]))
