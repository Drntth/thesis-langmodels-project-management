from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import UserProfile
from project_management.models import Project, ProjectMember
from ai_documentation.models import AIDocument
from pathlib import Path
from django.conf import settings
import shutil

class Command(BaseCommand):
    help = "Delete only Faker-generated data (users, projects, members, AI documents) and project folders"

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting Faker-generated data...")

        predefined_users = ["user", "staff", "superuser"]
        predefined_users_qs = User.objects.filter(username__in=predefined_users)

        AIDocument.objects.all().delete()
        ProjectMember.objects.all().delete()
        self.delete_project_folders()
        Project.objects.all().delete()
        UserProfile.objects.exclude(user__in=predefined_users_qs).delete()
        User.objects.exclude(id__in=predefined_users_qs.values_list('id', flat=True)).delete()

        self.stdout.write(self.style.SUCCESS("Faker-generated data has been deleted, but predefined users remain!"))

    def delete_project_folders(self):
        project_root_folder = Path(settings.MEDIA_ROOT) / "projects"

        if not project_root_folder.exists():
            self.stdout.write(self.style.WARNING("Project folders directory does not exist. Skipping deletion."))
            return

        for project in Project.objects.all():
            project_folder_name = f"{project.owner.username}_{project.name}".replace(' ', '_').lower()
            project_folder_path = project_root_folder / project_folder_name

            if project_folder_path.exists():
                try:
                    shutil.rmtree(project_folder_path)
                    self.stdout.write(self.style.SUCCESS(f"Deleted folder: {project_folder_path}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error deleting {project_folder_path}: {e}"))
            else:
                self.stdout.write(self.style.WARNING(f"Folder not found: {project_folder_path}"))
