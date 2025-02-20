from django.shortcuts import render, redirect, get_object_or_404
from .services import BaseModel
from .forms import TestModelForm, ProjectSelectionForm, DocumentSelectionForm
from django.views.generic import FormView, TemplateView, View
from django.contrib import messages
from django.urls import reverse
from project_management.models import Project
from ai_documentation.models import AIDocument
from pathlib import Path
from django.conf import settings

def generate_ai_text(ai_model, prompt, content):
    return BaseModel(ai_model.model_identifier).generate_text(prompt, content)

class TestModellsView(FormView):
    template_name="ai_models/test_models.html"
    form_class = TestModelForm

    def form_valid(self, form):
        ai_model = form.cleaned_data["ai_model"]
        prompt = form.cleaned_data["prompt"]
        model_identifier = ai_model.model_identifier

        try:
            ai_model_instance = BaseModel(model_identifier)
            generated_text = ai_model_instance.generate_text(prompt=prompt)

        except Exception as e:
            messages.error(self.request, f"Error while generating text: {str(e)}")
            return self.form_invalid(form)

        self.request.session["generated_text_data"] = {
            "prompt": prompt,
            "generated_text": generated_text,
            "model": model_identifier,
        }

        messages.success(self.request, "Text generated successfully!")
        return redirect(reverse("ai-models:test_generated_test"))

class TestGeneratedTextView(TemplateView):
    template_name = "ai_models/test_generated_text.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.request.session.pop("generated_text_data", None)
        if not data:
            context["error"] = "No generated text data found."
        else:
            context.update(data)
        return context

class SelectProjectView(FormView):
    template_name = "ai_models/select_project.html"
    form_class = ProjectSelectionForm

    def form_valid(self, form):
        project_id = form.cleaned_data["project"].id
        self.request.session["selected_project_id"] = project_id
        return redirect(reverse("ai-models:select_document"))

class SelectDocumentView(FormView):
    template_name = "ai_models/select_document.html"
    form_class = DocumentSelectionForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        project_id = self.request.session.get("selected_project_id")

        if not project_id:
            messages.error(self.request, f"The project ID is missing from the session.")

        self.project = get_object_or_404(Project, id=project_id)
        kwargs["project"] = self.project
        return kwargs

    def form_valid(self, form):
        document_id = form.cleaned_data["document"].id
        self.request.session["selected_document_id"] = document_id
        return redirect(reverse("ai-models:generate"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project"] = self.project
        return context

class GenerateView(View):
    template_name = "ai_models/generate.html"

    def get(self, request):
        document_id = request.session.get("selected_document_id")

        if not document_id:
            messages.error(self.request, f"The document ID is missing from the session.")
            return render(request, self.template_name, {"sections": []})

        document = get_object_or_404(AIDocument, id=document_id)

        project_id = request.session.get("selected_project_id")
        project = get_object_or_404(Project, id=project_id)

        sections = []
        lines = document.content.split("\n")
        current_section = None
        section_content = []

        for line in lines:
            if line.startswith("#"):
                if current_section:
                    content_to_add = "\n".join(section_content).strip()
                    sections.append((current_section, content_to_add))

                if line.count("#") == 1:
                    current_section = None
                    section_content = []
                else:
                    current_section = line.strip()
                    section_content = []

            elif line == "---": 
                if current_section:
                    content_to_add = "\n".join(section_content).strip()
                    sections.append((current_section, content_to_add))
                current_section = None 
                section_content = []

            elif current_section and line:
                section_content.append(line)

        return render(request, self.template_name, {"document": document, "sections": sections, "project_description": project.description})
    
class GenerateSectionContentView(View):
    def post(self, request):
        project_id = request.session.get("selected_project_id")
        project = get_object_or_404(Project, id=project_id)
        document_id = request.session.get("selected_document_id")
        document = get_object_or_404(AIDocument, id=document_id)

        section_title = request.POST.get("section_title")
        section_content = request.POST.get("section_content")
        prompt = request.POST.get("prompt")
        action = request.POST.get("action")

        if not section_title or not section_content:
            messages.error(request, "Missing title or content!")
            return redirect(reverse("ai-models:generate"))

        if action == "generate":
            try:
                generated_content = generate_ai_text(document.ai_model, prompt, section_content)

                lines = document.content.split("\n")
                new_lines = []
                inside_section = False

                for line in lines:
                    if line.strip() == section_title:
                        inside_section = True
                        new_lines.append(line)
                        new_lines.append(generated_content)

                    elif line.strip() == "---" and inside_section:
                        inside_section = False
                        new_lines.append(line)

                    elif not inside_section:
                        new_lines.append(line)

                document.content = "\n".join(new_lines)
                document.save()

                messages.success(request, f"The '{section_title}' section's content has been updated with AI-generated text!")

            except Exception as e:
                messages.error(request, f"Error while generating text: {str(e)}")

            return redirect(reverse("ai-models:generate"))

        elif action == "save":
            project_folder_name = f"{project.owner}_{project.name}".replace(' ', '_').lower()
            project_folder_path = Path(settings.MEDIA_ROOT) / "projects" / project_folder_name
            document_filename = f"{document.title}".replace(' ', '_').lower() + ".md"
            document_file_path = project_folder_path / document_filename

            if not project_folder_path.exists():
                messages.error(self.request, f"Project folder does not exist: {project_folder_name}")
            else:
                try:
                    with open(document_file_path, 'w', encoding='utf-8') as md_file:
                        md_file.write(document.content)

                    messages.success(self.request, f"Document '{document.title}' successfully updated! File saved: {document_filename}")
                except Exception as e:
                    messages.error(self.request, f"Error saving document file: {e}")

            return redirect(reverse("ai-models:generate"))
