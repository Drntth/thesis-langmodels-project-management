from django.apps import AppConfig


class AiDocumentationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ai_documentation'

    def ready(self):
        import ai_documentation.signals
