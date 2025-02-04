from django.db import models
from django.contrib.auth.models import User
from project_management.models import Project

class DocumentType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'Type: {self.name}'

class AIModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    model_identifier = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'Model: {self.name}'

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
