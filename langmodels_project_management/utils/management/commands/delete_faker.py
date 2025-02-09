from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from project_management.models import Project, ProjectMember
from ai_documentation.models import AIDocument

class Command(BaseCommand):
    help = "Delete only Faker-generated data (users, projects, members, AI documents)"

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting Faker-generated data...")

        AIDocument.objects.all().delete()
        ProjectMember.objects.all().delete()
        Project.objects.all().delete()
        # User.objects.exclude(is_superuser=True).delete()
        User.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Faker-generated data has been deleted!"))
