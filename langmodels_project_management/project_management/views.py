from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Project, ProjectMember
from .forms import ProjectCreationForm, ProjectUpdateForm, ProjectMemberForm
from django.urls import reverse_lazy
from django.contrib import messages
from pathlib import Path
from django.conf import settings
import os, shutil
from utils.clean_filename import clean_filename
from django.db.models import Q
from django.contrib.auth.models import User

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = "project_management/create_project.html"
    success_url = reverse_lazy('projects:list_projects')

    def form_valid(self, form):
        form.instance.owner = self.request.user 
        
        response = super().form_valid(form)

        project_folder_name = clean_filename(f"{self.request.user.username}_{form.instance.name}")
        project_folder_path = Path(settings.MEDIA_ROOT) / "projects" / project_folder_name
        
        if not project_folder_path.exists():
            project_folder_path.mkdir(parents=True, exist_ok=True)

        messages.success(self.request, f"Project '{form.instance.name}' successfully created!")
        return response

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "project_management/list_projects.html"
    context_object_name = "projects"

    def get_queryset(self):
        if self.request.user.is_staff:
            return Project.objects.all()
        return Project.objects.filter(
            Q(owner=self.request.user) | 
            Q(projectmember__user=self.request.user)
        ).distinct()

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "project_management/detail_project.html"
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["members"] = ProjectMember.objects.filter(project=self.object)
        context["is_project_member"] = ProjectMember.objects.filter(
            project=self.object, user=self.request.user
        ).exists()
        return context

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name = 'project_management/update_project.html'

    def get_success_url(self):
        return reverse_lazy('projects:detail_project', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        if self.request.user.is_staff:
            return Project.objects.all()
        return Project.objects.filter(
            Q(owner=self.request.user) |
            Q(projectmember__user=self.request.user)
        ).distinct()
    
    def form_valid(self, form):
        project = self.get_object()
        old_folder_path = self.get_project_folder_path(project)
        response = super().form_valid(form)

        if project.name != form.cleaned_data['name']:
            new_folder_path = self.get_project_folder_path(form.instance)

            if old_folder_path.exists():
                os.rename(old_folder_path, new_folder_path)
                messages.success(self.request, f"Project folder renamed to '{new_folder_path.name}'")

        messages.success(self.request, f"Project details for '{form.instance.name}' successfully updated!")
        return response

    def get_project_folder_path(self, project):
        project_root_folder = Path(settings.MEDIA_ROOT) / "projects"
        project_folder_name = clean_filename(f"{project.owner.username}_{project.name}")
        return project_root_folder / project_folder_name

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "project_management/delete_project.html"
    success_url = reverse_lazy("projects:list_projects") 

    def get_queryset(self):
        if self.request.user.is_staff:
            return Project.objects.all()
        return Project.objects.filter(
            Q(owner=self.request.user) |
            Q(projectmember__user=self.request.user)
        ).distinct()

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
        project_folder_name = clean_filename(f"{project.owner.username}_{project.name}")
        return project_root_folder / project_folder_name

class ProjectMemberCreateView(LoginRequiredMixin, CreateView):
    model = ProjectMember
    form_class = ProjectMemberForm
    template_name = "project_management/add_member.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['project'] = get_object_or_404(Project, id=self.kwargs['pk'])
        return kwargs

    def form_valid(self, form):
        project = get_object_or_404(Project, id=self.kwargs['pk'])
        form.instance.project = project
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error('user', 'The user is already a member of this project!')
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('projects:detail_project', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, id=self.kwargs['pk'])
        context['user_list'] = User.objects.all()
        return context

class ProjectMemberRemoveView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ProjectMember
    template_name = "project_management/detail_project.html"

    def get_success_url(self):
        return reverse_lazy('projects:detail_project', kwargs={'pk': self.object.project.id})

    def test_func(self):
        project = self.get_object().project
        return self.request.user.is_staff or self.request.user == project.owner

    def handle_no_permission(self):
        messages.error(self.request, "You do not have permission to remove this member.")
        return redirect('projects:detail_project', pk=self.get_object().project.id)