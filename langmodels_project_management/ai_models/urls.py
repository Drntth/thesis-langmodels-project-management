from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    TestModellsView,
    TestGeneratedTextView,
    SelectProjectView,
    SelectDocumentView,
    GenerateView,
    GenerateSectionContentView,
    GenerateDescriptionView,
    GenerateTitleView,
    ResultsView,
)

app_name = "ai-models"

urlpatterns = [
    path("test-models", TestModellsView.as_view(), name="test_models"),
    path(
        "test-generated-text",
        TestGeneratedTextView.as_view(),
        name="test_generated_text",
    ),
    path("select-project", SelectProjectView.as_view(), name="select_project"),
    path("select-document", SelectDocumentView.as_view(), name="select_document"),
    path("generate", GenerateView.as_view(), name="generate"),
    path(
        "generate/section-content",
        GenerateSectionContentView.as_view(),
        name="generate_section_content",
    ),
    path(
        "generate-description",
        GenerateDescriptionView.as_view(),
        name="generate_description",
    ),
    path("generate-title", GenerateTitleView.as_view(), name="generate_title"),
    path("results/", ResultsView.as_view(), name="results"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
