from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import CustomUser, CustomUserRating


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_type']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)


class UserRatingForm(forms.ModelForm):
    score = forms.IntegerField(required=False)

    class Meta:
        model = CustomUserRating
        fields = ['score']

    def clean(self):
        cleaned_data = super().clean()
        score = cleaned_data.get('score')
        if score is None:
            cleaned_data['score'] = 0  # Assign a default value if score is not provided
        return cleaned_data


class EditProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password')
