from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView
from .models import AIDocument
from .forms import DocumentCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from pathlib import Path
from django.conf import settings

class DocumentCreateView(LoginRequiredMixin, CreateView):
    model = AIDocument
    form_class = DocumentCreationForm
    template_name = "ai_documentation/create_document.html"
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        form.instance.created_by = self.request.user 

        try:
            form.instance.content = form.instance.type.get_template_file_content()
        except Exception as e:
            messages.error(self.request, f"Error loading document template: {e}")
            return self.form_invalid(form)

        response = super().form_valid(form)

        project = form.instance.project
        project_folder_name = f"{project.owner}_{project.name}".replace(' ', '_').lower()
        project_folder_path = Path(settings.MEDIA_ROOT) / "projects" / project_folder_name

        document_filename = f"{form.instance.title}".replace(' ', '_').lower() + ".md"
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

class DocumentDetailView(LoginRequiredMixin, DetailView):
    model = AIDocument
    template_name = "ai_documentation/detail_document.html"
    context_object_name = "document"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["members"] = ProjectMember.objects.filter(project=self.object)
    #     return context