from django.db import models

class AIModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    model_identifier = models.CharField(max_length=255, unique=True)
    local_path = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.name} ({self.model_identifier})'