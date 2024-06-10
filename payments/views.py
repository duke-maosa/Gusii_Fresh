from django.shortcuts import redirect, render
from django.urls import reverse
from django.conf import settings
import requests
from orders.models import Order

def initiate_payment(request):
    # Assuming `order` contains information about the order being paid for
    order = Order.objects.first()  # You need to fetch the order object from the database

    if order:
        order_total = order.calculate_total()

        # Prepare data for M-Pesa payment
        payload = {
            "BusinessShortCode": settings.MPESA_BUSINESS_SHORTCODE,
            "Password": settings.MPESA_PASSWORD,
            "Timestamp": settings.MPESA_TIMESTAMP,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": order_total,
            "PartyA": request.user.phone_number,  # Replace with customer's phone number
            "PartyB": settings.MPESA_BUSINESS_SHORTCODE,
            "PhoneNumber": request.user.phone_number,  # Replace with customer's phone number
            "CallBackURL": request.build_absolute_uri(reverse('mpesa_callback')),  # Callback URL for transaction status
            "AccountReference": f"Highland Fresh - {order.id}",  # Use a unique order reference
            "TransactionDesc": "Payment for order"  # Replace with description of the transaction
        }

        # Make request to M-Pesa API to initiate payment
        response = requests.post(settings.MPESA_PAYMENT_API_URL, json=payload, headers={'Authorization': f'Bearer {settings.MPESA_ACCESS_TOKEN}'})

        if response.status_code == 200:
            # Extract payment URL from the response
            payment_url = response.json().get('CheckoutRequestID')

            # Redirect users to the M-Pesa payment portal
            return redirect(payment_url)
        else:
            # Handle error in initiating payment
            return redirect('payment_failure')
    else:
        # Handle error when no order is found
        return redirect('payment_failure')

def payment_success(request):
    # Render the payment success template
    return render(request, 'payments/payment_success.html')

def payment_failure(request):
    # Render the payment failure template
    return render(request, 'payments/payment_failure.html')
