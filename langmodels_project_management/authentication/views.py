from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import CustomLoginForm, CustomRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from users.models import UserProfile

class CustomLoginView(LoginView):
    template_name = "authentication/login.html"
    authentication_form = CustomLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        messages.success(self.request, "You have successfully logged in!")
        return reverse_lazy("home:index")

class CustomRegisterView(CreateView):
    template_name = "authentication/register.html"
    form_class = CustomRegisterForm
    model = User
    success_url = reverse_lazy("home:index")
    
    def form_valid(self, form):
        user = form.save()
        UserProfile.objects.create(user=user)
        login(self.request, user) 
        messages.success(self.request, "Your account has been created successfully!")
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("authentication:login")

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been logged out.")
        return super().dispatch(request, *args, **kwargs)