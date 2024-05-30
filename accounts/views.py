from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import CustomUser, CustomUserRating
from .forms import RegistrationForm, LoginForm, UserRatingForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def rate_user(request, user_id):
    user_to_rate = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = UserRatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['score']
            CustomUserRating.objects.update_or_create(
                user=user_to_rate,
                rated_by=request.user,
                defaults={'score': rating}
            )
            # Update the overall rating of the user
            all_ratings = CustomUserRating.objects.filter(user=user_to_rate)
            average_rating = all_ratings.aggregate(models.Avg('score'))['score__avg']
            user_to_rate.rating = average_rating
            user_to_rate.save()
            messages.success(request, f'You have rated {user_to_rate.username}.')
            return redirect('profile')
    else:
        form = UserRatingForm()
    return render(request, 'accounts/rate_user.html', {'form': form, 'user_to_rate': user_to_rate})
