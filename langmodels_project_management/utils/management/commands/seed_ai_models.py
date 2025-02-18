from django.core.management.base import BaseCommand
from ai_models.models import AIModel

class Command(BaseCommand):
    help = "Seed the databse with AI models"

    def handle(self, *args, **kwargs):
        ai_models = [
            ("DistilGPT2", "distilbert/distilgpt2"), # 88.2M
            
            ("GPT-Neo 125M", "EleutherAI/gpt-neo-125m"), # 150M
            ("Facebook OPT 125M", "facebook/opt-125m"), # 125M

            ("GPT-2 Medium", "openai-community/gpt2-medium"), # 380M
            ("Facebook OPT 350M", "facebook/opt-350m"), # 350M
        ]

        created_models = []

        for name, identifier in ai_models:
            obj, created = AIModel.objects.get_or_create(name=name, model_identifier=identifier)
            if created:
                created_models.append(f"{name} -> {identifier}")

        if created_models:
            self.stdout.write(self.style.SUCCESS("Seeded AI models:"))
            for model in created_models:
                self.stdout.write(f" - {model}")
        else:
            self.stdout.write(self.style.WARNING("AI models already exist. No new models added."))
