from django.shortcuts import render
from products.models import Product
from account.models import CustomUser
from django.db.models import Q

def search(request):
    query = request.GET.get('q', '')
    sort_by = request.GET.get('sort_by', 'name')
    order = request.GET.get('order', 'asc')

    if query:
        sellers = CustomUser.objects.filter(user_type='seller', username__icontains=query)
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        buyers = CustomUser.objects.filter(user_type='buyer', username__icontains=query)
        
        if order == 'desc':
            sort_by = '-' + sort_by
        products = products.order_by(sort_by)

        context = {
            'sellers': sellers,
            'products': products,
            'buyers': buyers,
            'query': query,
            'sort_by': sort_by,
            'order': order,
        }
    else:
        context = {}

    return render(request, 'search/search_results.html', context)
