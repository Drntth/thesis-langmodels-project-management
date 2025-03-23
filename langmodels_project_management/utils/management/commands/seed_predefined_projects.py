from django.core.management.base import BaseCommand
from project_management.models import Project, ProjectStatus
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Seed the database with predefined projects"

    def handle(self, *args, **kwargs):
        superuser, created = User.objects.get_or_create(
            username="superuser",
            defaults={
                "is_superuser": True,
                "is_staff": True,
                "is_active": True,
            },
        )

        projects_data = [
            {
                "name": "Project Alpha",
                "description": "This is the first project.",
                "deadline": "2023-12-31",
                "status": "In Progress",
            },
            {
                "name": "Project Beta",
                "description": "This is the second project.",
                "deadline": "2024-01-15",
                "status": "Draft",
            },
            {
                "name": "Project Gamma",
                "description": "This is the third project.",
                "deadline": "2024-02-01",
                "status": "Completed",
            },
        ]

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                name=project_data["name"],
                defaults={
                    "description": project_data["description"],
                    "deadline": project_data["deadline"],
                    "owner": superuser,
                    "status": ProjectStatus.objects.get(name=project_data["status"]),
                },
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Project "{project.name}" created successfully.'
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Project "{project.name}" already exists.')
                )

        self.stdout.write(self.style.SUCCESS("Seeding predefined projects completed"))
