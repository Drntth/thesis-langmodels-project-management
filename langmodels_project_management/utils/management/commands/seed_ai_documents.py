import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from ai_documentation.models import AIDocument, AIModel, DocumentType
from project_management.models import Project
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Seed AI-generated documents"

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()

        users = list(User.objects.all())
        projects = list(Project.objects.all())
        ai_models = list(AIModel.objects.all())
        document_types = list(DocumentType.objects.all())

        if not users or not projects or not ai_models or not document_types:
            self.stdout.write(self.style.ERROR("Missing required data! Run seed_users, seed_projects, seed_ai_models, and seed_document_types first."))
            return

        num_documents = 10 
        seeder.add_entity(AIDocument, num_documents, {
            'title': lambda x: seeder.faker.sentence(),
            'content': lambda x: seeder.faker.paragraph(nb_sentences=5),
            'project': lambda x: random.choice(projects),
            'created_by': lambda x: random.choice(users),
            'version': 1,
            'type': lambda x: random.choice(document_types),
            'ai_model': lambda x: random.choice(ai_models),
        })

        inserted_pks = seeder.execute()
        created_documents = AIDocument.objects.filter(id__in=[pk for pk_list in inserted_pks.values() for pk in pk_list])

        self.stdout.write(self.style.SUCCESS(f"Seeded {num_documents} AI-generated documents:"))
        for doc in created_documents:
            self.stdout.write(f" - {doc.title} (Project: {doc.project.name}, Created by: {doc.created_by.username})")
