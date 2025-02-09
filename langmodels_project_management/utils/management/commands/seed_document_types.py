from django.core.management.base import BaseCommand
from ai_documentation.models import DocumentType

class Command(BaseCommand):
    help = "Seed the databse with document types"

    def handle(self, *args, **kwargs):
        document_types = ["Specification", "SRS"]
        created_types = []

        for doc_type in document_types:
            obj, created = DocumentType.objects.get_or_create(name=doc_type)
            if created:
                created_types.append(obj.name)

        if created_types:
            self.stdout.write(self.style.SUCCESS(f"Seeded document types: {', '.join(created_types)}"))
        else:
            self.stdout.write(self.style.WARNING("Document types already exist. No new types added."))
