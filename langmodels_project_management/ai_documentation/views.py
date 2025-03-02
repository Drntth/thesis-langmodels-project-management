from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, View
from .models import AIDocument
from .forms import DocumentCreationForm, DocumentUpdateForm
from django.urls import reverse_lazy
from django.contrib import messages
from pathlib import Path
from django.conf import settings
import os
from pathlib import Path
from django.http import FileResponse, Http404
from utils.clean_filename import clean_filename
from project_management.models import Project
from django.db.models import Q

class DocumentCreateView(LoginRequiredMixin, CreateView):
    model = AIDocument
    form_class = DocumentCreationForm
    template_name = "ai_documentation/create_document.html"
    success_url = reverse_lazy('ai-docs:list_documents')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.user = self.request.user 
        form.fields['project'].queryset = Project.objects.filter(owner=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.created_by = self.request.user 

        try:
            document_content = form.instance.type.get_template_file_content()

            context = {
                "project.name": form.instance.project.name,
                "document.version": 1,
                "document.created_by.username": form.instance.created_by.username,
                "document.ai_model.name": form.instance.ai_model.name if form.instance.ai_model else "N/A",
                "document.updated_at": "Not updated",
                "project.description": form.instance.project.description or "No description available",
            }

            for placeholder, value in context.items():
                document_content = document_content.replace(f'{{{{ {placeholder} }}}}', str(value))

            form.instance.content = document_content
        except Exception as e:
            messages.error(self.request, f"Error loading document template: {e}")
            return self.form_invalid(form)

        response = super().form_valid(form)

        project = form.instance.project
        project_folder_name = clean_filename(f"{project.owner.username}_{project.name}")
        project_folder_path = Path(settings.MEDIA_ROOT) / "projects" / project_folder_name

        document_filename = clean_filename(form.instance.title) + ".md"
        document_file_path = project_folder_path / document_filename

        if not project_folder_path.exists():
            messages.error(self.request, f"Project folder does not exist: {project_folder_name}")
        else:
            try:
                with open(document_file_path, 'w', encoding='utf-8') as md_file:
                    md_file.write(form.instance.content)

                messages.success(self.request, f"Document '{form.instance.title}' successfully created! File saved: {document_filename}")
            except Exception as e:
                messages.error(self.request, f"Error saving document file: {e}")

        return response

class DocumentListView(LoginRequiredMixin, ListView):
    model = AIDocument
    template_name = "ai_documentation/list_documents.html"
    context_object_name = "documents"

    def get_queryset(self):
        if self.request.user.is_staff:
            return AIDocument.objects.all()
        return AIDocument.objects.filter(
            Q(created_by=self.request.user) |  
            Q(project__projectmember__user=self.request.user)
        ).distinct()

class DocumentDetailView(LoginRequiredMixin, DetailView):
    model = AIDocument
    template_name = "ai_documentation/detail_document.html"
    context_object_name = "document"

class DocumentUpdateView(LoginRequiredMixin, UpdateView):
    model = AIDocument
    form_class = DocumentUpdateForm
    template_name = 'ai_documentation/update_document.html'

    def get_success_url(self):
        return reverse_lazy('ai-docs:detail_document', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        if self.request.user.is_staff:
            return AIDocument.objects.all()
        return AIDocument.objects.filter(created_by=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['document'] = self.object 
        return context
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.user = self.request.user 
        if self.request.user.is_staff:
            form.fields['project'].queryset = Project.objects.all()
        else:
            form.fields['project'].queryset = Project.objects.filter(owner=self.request.user)
        return form

    def form_valid(self, form):
        document = self.get_object()
        old_project = document.project
        new_project = form.cleaned_data['project']
        old_title = clean_filename(document.title) + ".md"
        new_title = clean_filename(form.cleaned_data['title'])+ ".md"
        new_content = form.cleaned_data['content']
        response = super().form_valid(form)

        old_folder_path = self.get_project_folder_path(old_project)
        new_folder_path = self.get_project_folder_path(new_project)
        old_file_path = old_folder_path / old_title
        new_file_path = new_folder_path / new_title

        if old_project == new_project:
            if old_title != new_title and old_file_path.exists():
                os.rename(old_file_path, new_file_path)
                messages.success(self.request, f"Document renamed to '{new_title}'")

            if new_file_path.exists():
                with open(new_file_path, "w", encoding="utf-8") as file:
                    file.write(new_content)
            else:
                with open(new_file_path, "w", encoding="utf-8") as file:
                    file.write(new_content)
        else:
            if old_file_path.exists():
                old_file_path.unlink()
            new_folder_path.mkdir(parents=True, exist_ok=True)
            with open(new_file_path, "w", encoding="utf-8") as file:
                file.write(new_content)
            messages.success(self.request, f"Document moved to project '{new_project.name}'")

        messages.success(self.request, f"Document details for '{new_title}' successfully updated!")
        return response

    def get_project_folder_path(self, project):
        project_root_folder = Path(settings.MEDIA_ROOT) / "projects"
        project_folder_name = clean_filename(f"{project.owner.username}_{project.name}")
        return project_root_folder / project_folder_name

class DocumentDeleteView(LoginRequiredMixin, DeleteView):
    model = AIDocument
    template_name = "ai_documentation/delete_document.html"
    success_url = reverse_lazy("ai-docs:list_documents") 

    def get_queryset(self):
        if self.request.user.is_staff:
            return AIDocument.objects.all()
        return AIDocument.objects.filter(created_by=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['document'] = self.object 
        return context

    def form_valid(self, form):
        document = self.get_object()
        project_folder_path = self.get_project_folder_path(document.project)
        file_name = clean_filename(document.title) + ".md"
        file_path = project_folder_path / file_name

        if file_path.exists():
            try:
                file_path.unlink()
                messages.success(self.request, f"Document '{file_name}' successfully deleted from project folder.")
            except Exception as e:
                messages.error(self.request, f"Failed to delete document '{file_name}': {e}")
        else:
            messages.warning(self.request, f"Document '{file_name}' not found in project folder.")

        return super().form_valid(form)

    def get_project_folder_path(self, project):
        project_root_folder = Path(settings.MEDIA_ROOT) / "projects"
        project_folder_name = clean_filename(f"{project.owner.username}_{project.name}")
        return project_root_folder / project_folder_name

class DocumentDownloadView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        document = get_object_or_404(AIDocument, id=pk)

        if not (request.user.is_staff or document.created_by == request.user):
            raise Http404("You do not have permission to access this document.")
    
        project = document.project

        project_folder_name = clean_filename(f"{project.owner.username}_{project.name}")
        project_folder_path = Path(settings.MEDIA_ROOT) / "projects" / project_folder_name
        document_filename = clean_filename(document.title) + ".md"
        document_file_path = project_folder_path / document_filename

        if not document_file_path.exists():
            raise Http404("File not found")

        response = FileResponse(document_file_path.open('rb'), as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{document_filename}"'
        return response