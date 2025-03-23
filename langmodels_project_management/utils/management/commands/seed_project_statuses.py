from django.core.management.base import BaseCommand
from project_management.models import ProjectStatus


class Command(BaseCommand):
    help = "Seed the database with project statuses"

    def handle(self, *args, **kwargs):
        statuses = ["Draft", "In Progress", "Completed"]
        created_statuses = []

        for status in statuses:
            obj, created = ProjectStatus.objects.get_or_create(name=status)
            if created:
                created_statuses.append(obj.name)

        if created_statuses:
            self.stdout.write(
                self.style.SUCCESS(f"Seeded statuses: {', '.join(created_statuses)}")
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    "Project statuses already exist. No new statuses added."
                )
            )
