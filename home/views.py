from django.shortcuts import render

def landing_page(request):
    return render(request, 'home/landing_page.html')

def about_us(request):
    return render(request, 'home/about_us.html')
