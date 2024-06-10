from django.shortcuts import render

def home(request):
    return render(request, 'home/base.html')

def index(request):
    return render(request, 'home/index.html')

def about_us(request):
    return render (request, 'about_us.html')
