from django.contrib import admin
from .models import DocumentType, AIDocument, DocumentSection


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(AIDocument)
class AIDocumentAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "project",
        "created_by",
        "created_at",
        "updated_at",
        "version",
        "type",
        "ai_model",
    )
    search_fields = ("title", "project__name", "created_by__username")
    list_filter = ("project", "created_by", "type", "ai_model")


@admin.register(DocumentSection)
class DocumentSectionAdmin(admin.ModelAdmin):
    list_display = ("document_type", "title")
    search_fields = ("title", "document_type__name")
    filter_horizontal = ("dependencies",)
