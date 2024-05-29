from django.shortcuts import render
from .models import CustomUserInteraction, SalesData

def dashboard(request):
    # Example: Get the count of user interactions
    interaction_count = CustomUserInteraction.objects.count()

    # Example: Get the total sales amount
    total_sales = SalesData.objects.aggregate(total=models.Sum('amount'))['total']

    context = {
        'interaction_count': interaction_count,
        'total_sales': total_sales,
    }
    return render(request, 'analytics/dashboard.html', context)
