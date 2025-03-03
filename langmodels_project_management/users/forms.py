from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class ProfileUpdateForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'id': 'username',
            'maxlength': 255, 
        })
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'id': 'email',
        })
    )
    first_name = forms.CharField(
        required=False,
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'id': 'first_name',
            'maxlength': 150,
        })
    )
    last_name = forms.CharField(
        required=False,
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'id': 'last_name',
            'maxlength': 150,
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'placeholder': 'Enter your current password...',
        })
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'placeholder': 'Enter your new password...'
        })
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'placeholder': 'Confirm your new password...'
        })
    )

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']