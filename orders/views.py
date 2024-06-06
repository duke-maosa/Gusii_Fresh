from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order
from cart.models import CartItem
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse




@login_required
def order_processing(request):
    # This view handles different actions based on the POST data
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'checkout':
            # Logic for handling the checkout process
            cart_items = CartItem.objects.filter(user=request.user)
            if not cart_items.exists():
                messages.warning(request, "Your cart is empty. Please add some items.")
                return redirect('view_cart')
            total_cost = sum(item.product.price * item.quantity for item in cart_items)
            order = Order.objects.create(user=request.user, total_cost=total_cost)
            order.items.set(cart_items)
            cart_items.delete()
            return redirect('order_confirmation', order_id=order.id)
        else:
            # Handle other actions if necessary
            pass
    else:
        # Redirect to the checkout page if the request method is GET
        cart_items = CartItem.objects.filter(user=request.user)
        total_cost = sum(item.product.price * item.quantity for item in cart_items)
        return render(request, 'orders/checkout.html', {'cart_items': cart_items, 'total_cost': total_cost})

    # Add a default return statement in case the request method is POST
    return HttpResponse("Order is being processed")


@login_required
def order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_details.html', {'order': order})

@login_required
def order_tracking(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    tracking_id = order.tracking_id  # Assume there's a tracking_id field in the Order model
    return render(request, 'orders/order_tracking.html', {'order_id': order_id, 'tracking_id': tracking_id})

@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.is_completed:
        messages.error(request, "This order has already been processed and cannot be canceled.")
    else:
        order.delete()  # Or update order status as canceled
        messages.success(request, "Order canceled successfully.")
    return redirect('order_history')
