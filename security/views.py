from django.shortcuts import render

def enable_2fa(request):
    return render(request, 'security/enable_2fa.html')
