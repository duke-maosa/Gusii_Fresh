# views.py

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.models import CartItem

@login_required
def order_processing(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'checkout':
            cart_items = CartItem.objects.filter(user=request.user)
            if not cart_items.exists():
                messages.warning(request, "Your cart is empty. Please add some items.")
                return redirect('cart:view_cart')
            
            order = Order.objects.create(user=request.user)
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )
            
            order.calculate_total_cost()
            cart_items.delete()
            
            return redirect('orders:order_summary', order_id=order.id)
        else:
            # Handle other actions if necessary
            pass
    else:
        cart_items = CartItem.objects.filter(user=request.user)
        total_cost = sum(item.product.price * item.quantity for item in cart_items)
        return render(request, 'orders/checkout.html', {'cart_items': cart_items, 'total_cost': total_cost})

@login_required
def order_summary(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = order.order_items.all()
    return render(request, 'orders/order_summary.html', {'order': order, 'order_items': order_items})


@login_required
def order_tracking(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    tracking_id = order.tracking_id  # Assuming there's a tracking_id field in the Order model
    return render(request, 'orders/order_tracking ', {'order_id': order_id, 'tracking_id': tracking_id})

@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.is_completed:
        messages.error(request, "This order has already been processed and cannot be canceled.")
    else:
        order.delete()  # Or update order status as canceled
        messages.success(request, "Order canceled successfully.")
    return redirect('orders:order_history')
