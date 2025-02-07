from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, View
from .forms import CustomLoginForm, CustomRegisterForm
from django.urls import reverse_lazy
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
    
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
            UserProfile.objects.create(user=user)
            messages.success(self.request, "Your account has been created successfully!")
            messages.success(self.request, "You have successfully logged in!")
            return redirect("home:index")
        else:
            messages.warning(self.request, "Authentication failed. Please try logging in manually.")
            return redirect("authentication:login")

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("authentication:login")

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been logged out.")
        return super().dispatch(request, *args, **kwargs)

class UseAsGuestView(View):
    def post(self, request, *args, **kwargs):
        messages.warning(request, "You are browsing as a guest. Some features may be unavailable.")
        return redirect(reverse_lazy("home:index"))