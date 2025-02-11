import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from ai_documentation.models import AIDocument, AIModel, DocumentType
from project_management.models import Project
from django.contrib.auth.models import User
from pathlib import Path
from django.conf import settings

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
        documents = []

        for _ in range(num_documents):
            document_type = random.choice(document_types)
            project = random.choice(projects)
            created_by = random.choice(users)
            ai_model = random.choice(ai_models)
            title = seeder.faker.sentence()
            content = document_type.get_template_file_content()

            document = AIDocument.objects.create(
                title=title,
                content=content,
                project=project,
                created_by=created_by,
                version=1,
                type=document_type,
                ai_model=ai_model,
            )

            project_folder_name = f"{project.owner}_{project.name}".replace(' ', '_').lower()
            project_folder_path = Path(settings.MEDIA_ROOT) / "projects" / project_folder_name
            document_filename = f"{document.title}".replace(' ', '_').lower() + ".md"
            document_file_path = project_folder_path / document_filename

            if not project_folder_path.exists():
                project_folder_path.mkdir(parents=True, exist_ok=True)

            try:
                with open(document_file_path, 'w', encoding='utf-8') as md_file:
                    md_file.write(document.content)

                documents.append(document)
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error saving document file: {e}"))

        self.stdout.write(self.style.SUCCESS(f"Seeded {len(documents)} AI-generated documents:"))
        for doc in documents:
            self.stdout.write(f" - {doc.title} (Project: {doc.project.name}, Created by: {doc.created_by.username})")
