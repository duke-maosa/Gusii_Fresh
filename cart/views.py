from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_cost = sum(item.total_price() for item in cart_items)
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items, 'total_cost': total_cost})

@login_required
def add_to_cart(request, product_id):
    # Logic to add product to cart
    pass

@login_required
def remove_from_cart(request, cart_item_id):
    # Logic to remove product from cart
    pass

@login_required
def update_cart(request, cart_item_id):
    # Logic to update cart
    pass
