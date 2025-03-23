from django.core.management.base import BaseCommand
from project_management.models import ProjectRole


class Command(BaseCommand):
    help = "Seed the database with project roles"

    def handle(self, *args, **kwargs):
        roles = ["Owner", "Project Manager", "Developer", "Tester", "Viewer"]
        created_roles = []

        for role in roles:
            obj, created = ProjectRole.objects.get_or_create(name=role)
            if created:
                created_roles.append(obj.name)

        if created_roles:
            self.stdout.write(
                self.style.SUCCESS(f"Seeded roles: {', '.join(created_roles)}")
            )
        else:
            self.stdout.write(
                self.style.WARNING("Project roles already exist. No new roles added.")
            )
