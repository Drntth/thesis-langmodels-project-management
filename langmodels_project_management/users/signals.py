from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command

@receiver(post_migrate)
def run_users_seeders(sender, **kwargs):
    if sender.name == "users":
        call_command("seed_predefined_users")