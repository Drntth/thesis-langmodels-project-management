from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command

@receiver(post_migrate)
def run_ai_models_seeders(sender, **kwargs):
    if sender.name == "ai_models":
        call_command("seed_ai_models")