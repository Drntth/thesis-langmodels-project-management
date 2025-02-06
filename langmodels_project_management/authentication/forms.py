from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'placeholder': 'Enter your username...',
            'id': 'username',
            'maxlength': 150,
        })
    )
    password = forms.CharField(
        required=True,
        max_length=255,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'placeholder': 'Enter your password...',
            'id': 'password',
            'maxlength': 255,
        })
    )

class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'placeholder': 'Enter your username...',
            'id': 'username',
            'maxlength': 150,
        })
    )
    email = forms.EmailField(
        required=True,
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'placeholder': 'Enter your email address...',
            'id': 'email',
            'maxlength': 254,
        })
    )
    first_name = forms.CharField(
        required=False,
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'placeholder': 'Enter your first name here...',
            'id': 'first_name',
            'maxlength': '150',
        })
    )
    last_name = forms.CharField(
        required=False,
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'placeholder': 'Enter your last name here...',
            'id': 'last_name',
            'maxlength': '150',
        })
    )
    password1  = forms.CharField(
        required=True,
        max_length=255,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'placeholder': 'Enter your password...',
            'id': 'password',
            'maxlength': 255,
        })
    )
    password2 = forms.CharField(
        required=True,
        max_length=255,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'placeholder': 'Confirm your password...',
            'id': 'confirm_password',
            'maxlength': 255,
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
