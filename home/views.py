from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def home(request):
    return render(request, 'home/base.html')

def index(request):
    return render(request, 'home/index.html')

def about_us(request):
    return render (request, 'home/about_us.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home:index')  # Redirect to the home page after successful form submission
    else:
        form = ContactForm()
    return render(request, 'home/contact_us.html', {'form': form})