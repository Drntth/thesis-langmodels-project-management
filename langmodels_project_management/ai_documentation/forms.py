from django import forms
from .models import AIDocument, DocumentType
from ai_models.models import AIModel
from project_management.models import Project

class DocumentCreationForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'placeholder': 'Enter a document title...',
            'maxlength': 255,
        })
    )
    content = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control border-0 shadow-sm',
            'rows': 4,
            'disabled': 'disabled',
        })
    )
    project = forms.ModelChoiceField(
        queryset=Project.objects.none(),
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control border-0 shadow-sm',
        })
    )
    type = forms.ModelChoiceField(
        queryset=DocumentType.objects.all(),
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control border-0 shadow-sm',
        })
    )
    ai_model = forms.ModelChoiceField(
        queryset=AIModel.objects.all(),
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control border-0 shadow-sm',
        })
    )

    class Meta:
        model = AIDocument
        fields = ['title', 'content', 'project', 'type', 'ai_model']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        document = super().save(commit=False)
        if hasattr(self, 'user') and self.user:
            document.created_by = self.user
        if commit:
            document.save()
        return document

class DocumentUpdateForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'maxlength': 255,
        })
    )
    content = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control border-0 shadow-sm',
            'rows': 4,
        })
    )
    project = forms.ModelChoiceField(
        queryset=Project.objects.none(),
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control border-0 shadow-sm',
        })
    )
    type = forms.ModelChoiceField(
        queryset=DocumentType.objects.all(),
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control border-0 shadow-sm',
            'disabled': 'disabled',
        })
    )
    ai_model = forms.ModelChoiceField(
        queryset=AIModel.objects.all(),
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control border-0 shadow-sm',
        })
    )

    class Meta:
        model = AIDocument
        fields = ['title', 'content', 'project', 'type', 'ai_model']