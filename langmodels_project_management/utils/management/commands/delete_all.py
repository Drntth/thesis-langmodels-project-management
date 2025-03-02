from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import UserProfile
from project_management.models import (
    Project, ProjectStatus, ProjectMember, ProjectRole, 
)
from ai_documentation.models import (
    DocumentType, AIModel, AIDocument, DocumentSection
)
from pathlib import Path
from django.conf import settings
import shutil
from utils.clean_filename import clean_filename

class Command(BaseCommand):
    help = 'Delete all data from User, UserProfile, Project, ProjectStatus, ProjectMember, ProjectRole, DocumentType, AIModel and AIDocument tables and project folders'

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting all data...")

        AIDocument.objects.all().delete()
        AIModel.objects.all().delete()
        DocumentType.objects.all().delete()
        DocumentSection.objects.all().delete()
        ProjectMember.objects.all().delete()
        self.delete_project_folders()
        Project.objects.all().delete()
        ProjectStatus.objects.all().delete()
        ProjectRole.objects.all().delete()
        UserProfile.objects.all().delete()
        User.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("All seeded data has been deleted!"))

    def delete_project_folders(self):
        project_root_folder = Path(settings.MEDIA_ROOT) / "projects"

        if not project_root_folder.exists():
            self.stdout.write(self.style.WARNING("Project folders directory does not exist. Skipping deletion."))
            return

        for project in Project.objects.all():
            project_folder_name = clean_filename(f"{project.owner.username}_{project.name}")
            project_folder_path = project_root_folder / project_folder_name

            if project_folder_path.exists():
                try:
                    shutil.rmtree(project_folder_path)
                    self.stdout.write(self.style.SUCCESS(f"Deleted folder: {project_folder_path}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error deleting {project_folder_path}: {e}"))
            else:
                self.stdout.write(self.style.WARNING(f"Folder not found: {project_folder_path}"))