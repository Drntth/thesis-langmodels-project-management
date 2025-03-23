from django.urls import path
from .views import (
    DocumentCreateView,
    DocumentListView,
    DocumentDetailView,
    DocumentUpdateView,
    DocumentDeleteView,
    DocumentDownloadView,
)
from django.conf import settings
from django.conf.urls.static import static

app_name = "ai-docs"

urlpatterns = [
    path("create", DocumentCreateView.as_view(), name="create_document"),
    path("list", DocumentListView.as_view(), name="list_documents"),
    path("<int:pk>/", DocumentDetailView.as_view(), name="detail_document"),
    path("<int:pk>/update", DocumentUpdateView.as_view(), name="update_document"),
    path("<int:pk>/delete", DocumentDeleteView.as_view(), name="delete_document"),
    path("<int:pk>/download", DocumentDownloadView.as_view(), name="download_document"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
