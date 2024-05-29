from django.shortcuts import render
from django.http import HttpResponse

def newsletter_signup(request):
    if request.method == 'POST':
        # Logic to handle newsletter signup form submission
        return HttpResponse('Thank you for signing up!')
    return render(request, 'marketing/newsletter_signup.html')
