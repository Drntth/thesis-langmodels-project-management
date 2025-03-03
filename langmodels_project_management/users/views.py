from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, View
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from .forms import ProfileUpdateForm, CustomPasswordChangeForm
from django.contrib import messages

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "users/detail_profile.html"
    context_object_name = "user"

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = self.get_object()
        if user.is_superuser:
            profile_picture = "/static/images/default_superuser.svg"
        elif user.is_staff:
            profile_picture = "/static/images/default_staff.svg"
        else:
            profile_picture = "/static/images/default_user.svg"

        context["profile_picture"] = profile_picture
        return context

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'users/update_profile.html'
    success_url = reverse_lazy('users:detail_profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your profile has been updated successfully.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "There was an error updating your profile. Please check the form and try again.")
        return self.render_to_response(self.get_context_data(form=form))

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:detail_profile')

    def form_valid(self, form):
        messages.success(self.request, "Your password has been updated successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error updating your password. Please check the form and try again.")
        return super().form_invalid(form)

class ProfileDeleteView(LoginRequiredMixin, View):    
    def post(self, request, *args, **kwargs):
        user = request.user
        messages.success(request, "Your profile has been deleted successfully. You can continue as a guest or register again!")
        user.delete()
        return redirect(reverse_lazy("home:index"))