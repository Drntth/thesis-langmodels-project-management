from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Seed static data (AI models, document types, project roles, project statuses)"

    def handle(self, *args, **kwargs):
        call_command("seed_predefined_users")
        call_command("seed_ai_models")
        call_command("seed_document_types")
        call_command("seed_project_roles")
        call_command("seed_project_statuses")
        self.stdout.write(self.style.SUCCESS("Static data has been seeded!"))
