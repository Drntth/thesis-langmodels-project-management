from django.contrib import admin
from .models import AIModel

@admin.register(AIModel)
class AIModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'model_identifier')
    search_fields = ('name', 'model_identifier') 
    ordering = ('name',)
