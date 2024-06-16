from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from products.models import Product
from .models import CartItem
from orders.models import Order, OrderItem
from django.db import transaction
from django.views.decorators.http import require_POST

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_cost = sum(item.total_price() for item in cart_items)
    order = None

    if request.method == 'POST':
        try:
            with transaction.atomic():
                order = Order.objects.filter(user=request.user).first()
                if not order:
                    order = Order.objects.create(user=request.user)
                # Add cart items to order or any other order processing here
                messages.success(request, "Order placed successfully.")
        except Exception as e:
            messages.error(request, f"Error placing order: {str(e)}")
            return redirect('cart:view_cart')

    return render(request, 'cart/view_cart.html', {
        'cart_items': cart_items,
        'total_cost': total_cost,
        'order': order,
    })
def create_order(user, cart_items):
    try:
        total_cost = sum(item.total_price() for item in cart_items)
        order = Order.objects.create(user=user, total_cost=total_cost)
        OrderItem.objects.bulk_create([
            OrderItem(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            ) for item in cart_items
        ])
        return order
    except Exception as e:
        raise e

def clear_cart(user):
    try:
        CartItem.objects.filter(user=user).delete()
    except Exception as e:
        raise e

@require_POST
@login_required

def add_to_cart(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get('quantity', 1))

        if quantity > product.available_quantity:
            return JsonResponse({'error': 'Quantity exceeds available stock.'}, status=400)

        with transaction.atomic():
            cart_item, created = CartItem.objects.select_for_update().get_or_create(user=request.user, product=product)
            if created:
                cart_item.quantity = quantity
            else:
                cart_item.quantity += quantity

            if cart_item.quantity > product.available_quantity:
                return JsonResponse({'error': 'Quantity exceeds available stock.'}, status=400)

            cart_item.save()

        return JsonResponse({'message': 'Item added to cart successfully.'})

    except Exception as e:
        return JsonResponse({'error': f'Error adding item to cart: {str(e)}'}, status=500)


@login_required
def remove_from_cart(request, cart_item_id):
    try:
        cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
        cart_item.delete()
        messages.success(request, 'Item removed from cart.')
    except Exception as e:
        messages.error(request, f"Error removing item from cart: {str(e)}")
    return redirect('cart:view_cart')

@login_required
def update_cart(request, cart_item_id):
    try:
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
    except Exception as e:
        messages.error(request, f"Error updating cart: {str(e)}")
    return redirect('cart:view_cart')
