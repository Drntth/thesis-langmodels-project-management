from django import forms
from django.contrib.auth.models import User
from .models import Project

class ProjectCreationForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'placeholder': 'Enter a project name...',
            'id': 'name',
            'maxlength': 255,
        })
    )

    class Meta:
        model = Project
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        project = super().save(commit=False)
        if self.user:
            project.owner = self.user
        if commit:
            project.save()
        return project