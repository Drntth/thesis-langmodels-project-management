from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth.models import User

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "users/profile-read.html"
    context_object_name = "user_profile"

    def get_object(self):
        return self.request.user
