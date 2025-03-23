from django.shortcuts import render, redirect, get_object_or_404
from .services import PipelineTextGenerator
from .forms import (
    TestModelForm,
    ProjectSelectionForm,
    DocumentSelectionForm,
    GenerateDescriptionForm,
    GenerateTitleForm,
)
from django.views.generic import FormView, TemplateView, View
from django.contrib import messages
from django.urls import reverse
from project_management.models import Project, ProjectMember
from ai_documentation.models import AIDocument, DocumentSection
from ai_models.models import AIModel
from pathlib import Path
from django.conf import settings
from utils.clean_filename import clean_filename
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class TestModellsView(FormView):
    template_name = "ai_models/test_models.html"
    form_class = TestModelForm

    def form_valid(self, form):
        ai_model = form.cleaned_data["ai_model"]
        prompt = form.cleaned_data["prompt"]
        model_identifier = ai_model.model_identifier

        try:
            ai_model_instance = PipelineTextGenerator(model_identifier)
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
        return redirect(reverse("ai-models:test_generated_text"))


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


class SelectProjectView(LoginRequiredMixin, FormView):
    template_name = "ai_models/select_project.html"
    form_class = ProjectSelectionForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.user = self.request.user
        if self.request.user.is_staff:
            form.fields["project"].queryset = Project.objects.all()
        else:
            form.fields["project"].queryset = Project.objects.filter(
                Q(owner=self.request.user) | Q(projectmember__user=self.request.user)
            ).distinct()
        return form

    def form_valid(self, form):
        project_id = form.cleaned_data["project"].id
        self.request.session["selected_project_id"] = project_id
        return redirect(reverse("ai-models:select_document"))


class SelectDocumentView(LoginRequiredMixin, FormView):
    template_name = "ai_models/select_document.html"
    form_class = DocumentSelectionForm

    def get_queryset(self):
        if self.request.user.is_staff:
            return AIDocument.objects.all()
        return AIDocument.objects.filter(
            Q(created_by=self.request.user)
            | Q(project__projectmember__user=self.request.user)
        ).distinct()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        project_id = self.request.session.get("selected_project_id")

        if not project_id:
            messages.error(self.request, "The project ID is missing from the session.")

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


class GenerateView(LoginRequiredMixin, View):
    template_name = "ai_models/generate.html"

    def get(self, request):
        document_id = request.session.get("selected_document_id")

        if not document_id:
            messages.error(
                self.request, "The document ID is missing from the session."
            )
            return render(request, self.template_name, {"sections": []})

        document = get_object_or_404(AIDocument, id=document_id)

        project_id = request.session.get("selected_project_id")
        project = get_object_or_404(Project, id=project_id)

        is_project_member = ProjectMember.objects.filter(
            user=request.user, project=project
        ).exists()

        if not (
            request.user.is_staff
            or document.created_by == request.user
            or is_project_member
        ):
            messages.error(
                request, "You do not have permission to access this document."
            )
            return redirect("ai-models:select_document")

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

        return render(
            request,
            self.template_name,
            {
                "document": document,
                "sections": sections,
                "project_description": project.description,
            },
        )


class GenerateSectionContentView(LoginRequiredMixin, View):
    def post(self, request):
        project_id = request.session.get("selected_project_id")
        project = get_object_or_404(Project, id=project_id)
        document_id = request.session.get("selected_document_id")
        document = get_object_or_404(AIDocument, id=document_id)

        is_project_member = ProjectMember.objects.filter(
            user=request.user, project=project
        ).exists()

        if not (
            request.user.is_staff
            or document.created_by == request.user
            or is_project_member
        ):
            messages.error(
                request, "You do not have permission to modify this document."
            )
            return redirect(reverse("ai-models:generate"))

        section_title = request.POST.get("section_title").strip()
        section_content = request.POST.get("section_content").strip()
        action = request.POST.get("action")

        if not section_title or not section_content:
            messages.error(request, "Missing title or content!")
            return redirect(reverse("ai-models:generate"))

        try:
            doc_section = DocumentSection.objects.get(
                document_type=document.type, title=section_title
            )
            prompt = doc_section.prompt
            dependencies = doc_section.dependencies.all()
        except DocumentSection.DoesNotExist:
            messages.error(request, "No prompt found for this section in the database!")
            return redirect(reverse("ai-models:generate"))

        if action == "generate":
            try:
                if dependencies.exists():
                    dependencies_text = "\n".join(
                        [f"{dep.title}: {dep.prompt}" for dep in dependencies]
                    )
                    full_prompt = f"{prompt}\nDependencies:\n{dependencies_text}\n{section_content}"
                else:
                    full_prompt = f"{prompt}\n{section_content}"

                generated_content = PipelineTextGenerator(
                    document.ai_model.model_identifier
                ).generate_text(full_prompt)

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
                AIDocument.objects.filter(id=document.id).update(
                    content=document.content
                )

                messages.success(
                    request,
                    f"The '{section_title}' section's content has been updated with AI-generated text!",
                )

            except Exception as e:
                messages.error(request, f"Error while generating text: {str(e)}")

            return redirect(reverse("ai-models:generate"))

        elif action == "save":
            try:
                lines = document.content.split("\n")
                new_lines = []
                inside_section = False

                for i, line in enumerate(lines):
                    stripped_line = line.strip()

                    if stripped_line == section_title:
                        inside_section = True
                        new_lines.append(section_title)
                        new_lines.append("")
                        new_lines.extend(section_content.splitlines())

                    elif stripped_line == "---" and inside_section:
                        inside_section = False

                        if new_lines and new_lines[-1].strip():
                            new_lines.append("")

                        new_lines.append("---")

                    elif not inside_section:
                        new_lines.append(line)

                document.content = "\n".join(new_lines)
                document.save()

                project_folder_name = clean_filename(
                    f"{project.owner.username}_{project.name}"
                )
                project_folder_path = (
                    Path(settings.MEDIA_ROOT) / "projects" / project_folder_name
                )
                document_filename = clean_filename(document.title) + ".md"
                document_file_path = project_folder_path / document_filename

                if not project_folder_path.exists():
                    messages.error(
                        self.request,
                        f"Project folder does not exist: {project_folder_name}",
                    )
                else:
                    try:
                        with open(document_file_path, "w", encoding="utf-8") as md_file:
                            md_file.write(document.content)

                        messages.success(
                            self.request,
                            f"Document '{document.title}' successfully updated! File saved: {document_filename}",
                        )
                    except Exception as e:
                        messages.error(self.request, f"Error saving document file: {e}")

            except Exception as e:
                messages.error(request, f"Error updating section content: {e}")

            return redirect(reverse("ai-models:generate"))


class GenerateDescriptionView(FormView):
    template_name = "ai_models/generate_description.html"
    form_class = GenerateDescriptionForm

    def form_valid(self, form):
        ai_models = AIModel.objects.all()
        title = form.cleaned_data["title"]

        results = []

        for ai_model in ai_models:
            try:
                ai_model_instance = PipelineTextGenerator(ai_model.model_identifier)
                prompt = f"Please write a professional and structured project description of an '{title}' project title. Include key features, benefits, and possible applications in the workplace."
                generated_text = ai_model_instance.generate_text(
                    prompt=prompt,
                    min_new_tokens=50,
                    max_new_tokens=150,
                )

                results.append(
                    {
                        "model": ai_model.model_identifier,
                        "generated_text": generated_text,
                    }
                )

            except Exception as e:
                messages.error(self.request, f"Error while generating text: {str(e)}")
                return self.form_invalid(form)

        self.request.session["generated_results"] = {"title": title, "results": results}

        messages.success(self.request, "Text generated successfully!")
        return redirect(reverse("ai-models:results"))


class GenerateTitleView(FormView):
    template_name = "ai_models/generate_title.html"
    form_class = GenerateTitleForm

    def form_valid(self, form):
        ai_models = AIModel.objects.all()
        description = form.cleaned_data["description"]

        results = []

        for ai_model in ai_models:
            try:
                ai_model_instance = PipelineTextGenerator(ai_model.model_identifier)
                prompt = f"Given the following project description, generate a concise, engaging, and informative title that accurately reflects its purpose and scope. The title should be clear, professional, and no longer than 10 words. Do not include explanations, introductions, or additional text-only return the title itself. Project Description: '{description}'' The project title is:"
                generated_text = ai_model_instance.generate_text(
                    prompt=prompt,
                    min_new_tokens=10,
                    max_new_tokens=20,
                )

                results.append(
                    {
                        "model": ai_model.model_identifier,
                        "generated_text": generated_text,
                    }
                )

            except Exception as e:
                messages.error(self.request, f"Error while generating text: {str(e)}")
                return self.form_invalid(form)

        self.request.session["generated_results"] = {
            "description": description,
            "results": results,
        }

        messages.success(self.request, "Text generated successfully!")
        return redirect(reverse("ai-models:results"))


class ResultsView(TemplateView):
    template_name = "ai_models/results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.request.session.pop("generated_results", None)
        if not data:
            context["error"] = "No generated text data found."
        else:
            context.update(data)
        return context
