from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Avg
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from allauth.socialaccount.models import SocialAccount
from products.models import Product 
from .models import CustomUser, CustomUserRating
from .forms import RegistrationForm, LoginForm, EditProfileForm


def render_auth_form(request, form, template_name):
    social_accounts = SocialAccount.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, template_name, {'form': form, 'social_accounts': social_accounts, 'user': request.user})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home:index')
    else:
        form = RegistrationForm()
    return render_auth_form(request, form, 'account/register.html')


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
                next_url = request.GET.get('next', 'home:index')
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render_auth_form(request, form, 'account/login.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('home:index')

@login_required
def profile(request):
    user_ratings, created = CustomUserRating.objects.get_or_create(user=request.user, defaults={'rating': 0})
    return render(request, 'account/profile.html', {'user_ratings': user_ratings, 'user': request.user})

@login_required
def rate_user(request, user_id):
    user_to_rate = get_object_or_404(CustomUser, id=user_id)
    try:
        rating = float(request.POST.get('rating'))
        if 1 <= rating <= 5:
            CustomUserRating.objects.update_or_create(
                user=user_to_rate,
                rated_by=request.user,
                defaults={'rating': rating}
            )
            all_ratings = CustomUserRating.objects.filter(user=user_to_rate)
            average_rating = all_ratings.aggregate(Avg('rating'))['rating__avg']
            user_to_rate.rating = average_rating
            user_to_rate.save()
            messages.success(request, f'You have rated {user_to_rate.username}.')
        else:
            messages.error(request, 'Invalid rating. Please rate between 1 and 5.')
    except ValueError:
        messages.error(request, 'Invalid rating value.')
    return redirect('account:profile')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('account:profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'account/edit_profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully.')
            return redirect('account:profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'account/change_password.html', {'form': form})



@login_required
def sellers_page(request):
    # Get all sellers
    sellers = CustomUser.objects.filter(user_type='seller')

    # Calculate average rating for each seller
    seller_ratings = {}
    for seller in sellers:
        seller_avg_rating = CustomUserRating.objects.filter(user=seller).aggregate(Avg('rating'))['rating__avg']
        seller_ratings[seller.username] = seller_avg_rating

    context = {
        'sellers': sellers,
        'seller_ratings': seller_ratings,
    }

    return render(request, 'account/sellers.html', context)