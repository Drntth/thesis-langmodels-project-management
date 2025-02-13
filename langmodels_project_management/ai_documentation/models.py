from django.db import models
from django.contrib.auth.models import User
from project_management.models import Project
from django.templatetags.static import static
import os
from django.conf import settings
from ai_models.models import AIModel

class DocumentType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'

    def get_template_file_content(self):
        template_filename = f"{self.name.replace(' ', '_').lower()}.md"
        template_path = os.path.join(settings.STATICFILES_DIRS[0], "document", template_filename)

        if os.path.exists(template_path):
            try:
                with open(template_path, 'r', encoding='utf-8') as file:
                    return file.read()
            except Exception as e:
                return f"Error reading template file: {e}"

        return "Template file not found."

class AIDocument(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    version = models.IntegerField(default=1)
    type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    ai_model = models.ForeignKey(AIModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'Document: {self.title} (Project: {self.project})'
