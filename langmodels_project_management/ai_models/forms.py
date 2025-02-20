from django import forms
from .models import AIModel
from project_management.models import Project
from ai_documentation.models import AIDocument

class TestModelForm(forms.Form):
    ai_model = forms.ModelChoiceField(
        queryset=AIModel.objects.all(),
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control border-0 shadow-sm',
        })
    )

    prompt = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
        'class': 'form-control border-0 shadow-sm',
        'rows': 4,
        })
    )

    class Meta:
        fields = ['ai_model', 'prompt']

class ProjectSelectionForm(forms.Form):
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control border-0 shadow-sm',
        })
    )

class DocumentSelectionForm(forms.Form):
    def __init__(self, project, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["document"] = forms.ModelChoiceField(
            queryset=AIDocument.objects.filter(project=project),
            required=True,
            widget=forms.Select(attrs={
                'class': 'form-control border-0 shadow-sm',
            })
        )