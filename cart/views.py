from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from products.models import Product
from .models import CartItem


def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_cost = sum(item.total_price() for item in cart_items)

    if request.method == 'POST':
        order = create_order(request.user, cart_items)
        clear_cart(request.user)
        return HttpResponseRedirect(reverse('orders:order_summary', args=[order.id]))

    return render(request, 'cart/view_cart.html', {'cart_items': cart_items, 'total_cost': total_cost})
@login_required
def create_order(user, cart_items):
    from orders.models import Order, OrderItem  # Import within function to avoid circular import
    total_cost = sum(item.total_price() for item in cart_items)
    order = Order.objects.create(user=user, total_cost=total_cost)
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )
    return order

def clear_cart(user):
    CartItem.objects.filter(user=user).delete()


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    if quantity > product.available_quantity:
        messages.error(request, 'Quantity exceeds available stock.')
        return redirect('products:product_detail', product_id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    cart_item.quantity += quantity
    cart_item.save()
    messages.success(request, 'Item added to cart successfully.')
    return redirect('cart:view_cart')


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart.')
    return redirect('cart:view_cart')

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
