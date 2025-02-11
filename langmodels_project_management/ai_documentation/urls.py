from django.urls import path
from .views import DocumentCreateView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ai-docs'

urlpatterns = [
    path('create', DocumentCreateView.as_view(), name='create_document'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)