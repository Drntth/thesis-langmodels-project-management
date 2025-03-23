from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command


@receiver(post_migrate)
def run_ai_documentation_seeders(sender, **kwargs):
    if sender.name == "ai_documentation":
        call_command("seed_document_types")
        call_command("seed_section_prompts")
