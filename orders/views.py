from django.shortcuts import render, redirect
from .models import Order
from cart.models import CartItem
from django.contrib.auth.decorators import login_required

@login_required
def order_processing(request, action, order_id=None):
    if action == 'checkout':
        if request.method == 'POST':
            # Logic to handle the checkout process
            # Retrieve cart items for the current user
            cart_items = CartItem.objects.filter(user=request.user)
            # Calculate total cost
            total_cost = sum(item.product.price * item.quantity for item in cart_items)
            # Create order and save it
            order = Order.objects.create(user=request.user, total_cost=total_cost)
            order.items.set(cart_items)
            # Clear the user's cart
            cart_items.delete()
            return redirect('order_confirmation', order_id=order.id)
        else:
            # Retrieve cart items for the current user
            cart_items = CartItem.objects.filter(user=request.user)
            total_cost = sum(item.product.price * item.quantity for item in cart_items)
            return render(request, 'orders/checkout.html', {'cart_items': cart_items, 'total_cost': total_cost})
    
    elif action == 'details':
        order = Order.objects.get(id=order_id, user=request.user)
        return render(request, 'orders/order_details.html', {'order': order})
    
    elif action == 'tracking':
        # Logic to retrieve tracking information for the order
        return render(request, 'orders/order_tracking.html', {'order_id': order_id})
    
    elif action == 'cancel':
        order = Order.objects.get(id=order_id, user=request.user)
        if order.is_completed:
            # Order has already been processed, cannot be canceled
            # You might want to provide feedback to the user
            pass
        else:
            # Cancel the order and provide feedback to the user
            order.delete()  # Or update order status as canceled
            pass
        return redirect('order_history')

    else:
        # Invalid action, handle accordingly
        pass
