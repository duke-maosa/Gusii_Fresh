from django.shortcuts import render

def home(request):
    return render(request, 'home/kisii-fresh-st35s84/index.html')

def index(request):
    return render(request, 'home/kisii-fresh-st35s84/base.html')
