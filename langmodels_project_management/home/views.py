from django.shortcuts import render
from django.views.generic import TemplateView
from project_management.models import Project
from ai_documentation.models import AIDocument
from django.contrib.auth.models import User

class HomePageView(TemplateView):
    template_name = "home/index.html"
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = Project.objects.filter(
            name__in=["Project Alpha", "Project Beta", "Project Gamma"]
        )
        context["project_count"] = Project.objects.count()
        context["ai_document_count"] = AIDocument.objects.count()
        context["user_count"] = User.objects.count()
        return context