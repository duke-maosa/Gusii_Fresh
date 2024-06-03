from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CartItem, Product  # Assuming you have a Product model

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_cost = sum(item.total_price() for item in cart_items)
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items, 'total_cost': total_cost})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
    cart_item.save()
    messages.success(request, f'Added {product.name} to cart.')
    return redirect('cart:view_cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart.')
    return redirect('cart:view_cart')

@login_required
def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated.')
        else:
            cart_item.delete()
            messages.success(request, 'Item removed from cart.')

    return redirect('cart:view_cart')
