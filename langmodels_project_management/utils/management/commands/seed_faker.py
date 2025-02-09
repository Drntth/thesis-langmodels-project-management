from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Seed only Faker-generated data (users, projects, members, AI documents)"

    def handle(self, *args, **kwargs):
        call_command("seed_users")
        call_command("seed_projects")
        call_command("seed_project_members")
        call_command("seed_ai_documents")
        self.stdout.write(self.style.SUCCESS("Faker-generated data has been seeded!"))
