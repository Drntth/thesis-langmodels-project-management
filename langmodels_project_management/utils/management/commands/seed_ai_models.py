from django.core.management.base import BaseCommand
from ai_documentation.models import AIModel

class Command(BaseCommand):
    help = "Seed the databse with AI models"

    def handle(self, *args, **kwargs):
        ai_models = [
            ("Bloom (BigScience)", "bigscience/bloom-560m"),
            ("Bert (Google)", "bert-base-uncased"),
            ("GPT-Neo (EleutherAI)", "EleutherAI/gpt-neo-2.7B"),
            ("GPT-J (EleutherAI)", "EleutherAI/gpt-j-6b"),
            ("LLAMA (Meta AI)", "meta-llama/Llama-2-7b-hf"),
            ("DeepSeek-R1", "deepseek-ai/DeepSeek-R1"),
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
