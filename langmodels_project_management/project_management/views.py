from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from .models import Project, ProjectMember
from .forms import ProjectCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from pathlib import Path
from django.conf import settings
import os, shutil

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = "project_management/create_project.html"
    success_url = reverse_lazy('projects:list_projects')

    def form_valid(self, form):
        form.instance.owner = self.request.user 
        
        response = super().form_valid(form)

        project_folder_name = f"{self.request.user.username}_{form.instance.name}".replace(' ', '_').lower()
        project_folder_path = Path(settings.MEDIA_ROOT) / "projects" / project_folder_name
        
        if not project_folder_path.exists():
            project_folder_path.mkdir(parents=True, exist_ok=True)

        messages.success(self.request, f"Project '{form.instance.name}' successfully created!")
        return response

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "project_management/list_projects.html"
    context_object_name = "projects"

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "project_management/detail_project.html"
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["members"] = ProjectMember.objects.filter(project=self.object)
        return context

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "project_management/delete_project.html"
    success_url = reverse_lazy("projects:list_projects") 

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        project = self.get_object()
        project_folder_path = self.get_project_folder_path(project)

        if project_folder_path.exists():
            try:
                shutil.rmtree(project_folder_path)
                messages.success(self.request, f"Project '{project.name}' and its associated data have been successfully deleted!")
            except Exception as e:
                messages.error(self.request, f"Project '{project.name}' was deleted, but failed to remove associated data: {e}")
        else:
            messages.warning(self.request, f"Project '{project.name}' deleted, but no associated data was found.")

        return super().form_valid(form)

    def get_project_folder_path(self, project):
        project_root_folder = Path(settings.MEDIA_ROOT) / "projects"
        project_folder_name = f"{project.owner.username}_{project.name}".replace(' ', '_').lower()
        return project_root_folder / project_folder_name