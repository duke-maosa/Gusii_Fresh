from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def index(request):
    return render(request, 'home/base.html')
