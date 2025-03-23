from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Seed all data (both static and Faker-generated)"

    def handle(self, *args, **kwargs):
        call_command("seed_static")
        call_command("seed_faker")
        self.stdout.write(self.style.SUCCESS("All data has been seeded!"))
