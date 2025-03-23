from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command


@receiver(post_migrate)
def run_project_management_seeders(sender, **kwargs):
    if sender.name == "project_management":
        call_command("seed_project_roles")
        call_command("seed_project_statuses")
        call_command("seed_predefined_projects")
