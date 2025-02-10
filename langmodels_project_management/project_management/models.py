from django.db import models
from django.contrib.auth.models import User

class ProjectStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'Status: {self.name}'

class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(ProjectStatus, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'Project: {self.name} (Owner: {self.owner.username})'
    
    def save(self, *args, **kwargs):
        if not self.status_id:
            draft_status, created = ProjectStatus.objects.get_or_create(name="Draft")
            self.status = draft_status
        super().save(*args, **kwargs)

class ProjectRole(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'Role: {self.name}'

class ProjectMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.ForeignKey(ProjectRole, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f"{self.user.username} - {self.role.name} in {self.project.name}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.project.status.name == "Draft":
            in_progress_status, created = ProjectStatus.objects.get_or_create(name="In Progress")
            self.project.status = in_progress_status
            self.project.save()