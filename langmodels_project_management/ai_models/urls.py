from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import TestModellsView, TestGeneratedTextView

app_name = 'ai-models'

urlpatterns = [
  path('test-models', TestModellsView.as_view(), name='test_models'),
  path('test-generated-text', TestGeneratedTextView.as_view(), name='test_generated_test'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)