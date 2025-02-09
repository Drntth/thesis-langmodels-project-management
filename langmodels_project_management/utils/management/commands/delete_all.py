from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.auth.models import User
from users.models import UserProfile
from project_management.models import (
    Project, ProjectStatus, ProjectMember, ProjectRole, 
)
from ai_documentation.models import (
    DocumentType, AIModel, AIDocument
)
import random

class Command(BaseCommand):
    help = 'Delete all data from User, UserProfile, Project, ProjectStatus, ProjectMember, ProjectRole, DocumentType, AIModel and AIDocument tables'

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting all data...")

        AIDocument.objects.all().delete()
        AIModel.objects.all().delete()
        DocumentType.objects.all().delete()
        ProjectMember.objects.all().delete()
        Project.objects.all().delete()
        ProjectStatus.objects.all().delete()
        ProjectRole.objects.all().delete()
        UserProfile.objects.all().delete()
        # User.objects.exclude(is_superuser=True).delete()
        User.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("All seeded data has been deleted!"))