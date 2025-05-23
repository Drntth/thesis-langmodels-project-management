from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, View
from .forms import CustomLoginForm, CustomRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin


class CustomLoginView(UserPassesTestMixin, LoginView):
    template_name = "authentication/login.html"
    authentication_form = CustomLoginForm
    redirect_authenticated_user = True

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.warning(self.request, "You are already registered and logged in!")
        return redirect("home:index")

    def get_success_url(self):
        messages.success(self.request, "You have successfully logged in!")
        return reverse_lazy("home:index")


class CustomRegisterView(UserPassesTestMixin, CreateView):
    template_name = "authentication/register.html"
    form_class = CustomRegisterForm

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.warning(self.request, "You are already registered and logged in!")
        return redirect("home:index")

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
            messages.success(
                self.request, "Your account has been created successfully!"
            )
            messages.success(self.request, "You have successfully logged in!")
            return redirect("home:index")
        else:
            messages.warning(
                self.request, "Authentication failed. Please try logging in manually."
            )
            return redirect("authentication:login")


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("authentication:login")

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been logged out.")
        return super().dispatch(request, *args, **kwargs)


class UseAsGuestView(View):
    def post(self, request, *args, **kwargs):
        messages.warning(
            request, "You are browsing as a guest. Some features may be unavailable."
        )
        return redirect(reverse_lazy("home:index"))
