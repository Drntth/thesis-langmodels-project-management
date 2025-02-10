from django import forms
from .models import Project
import datetime

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
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control border-0 shadow-sm',
            'placeholder': 'Enter a project description (optional)...',
            'rows': 4,
        })
    )
    deadline = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control border-0 shadow-sm',
            'type': 'date',
            'min': datetime.date.today().strftime('%Y-%m-%d'),
        })
    )

    class Meta:
        model = Project
        fields = ['name', 'description', 'deadline']

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

    def clean_deadline(self):
        deadline = self.cleaned_data.get('deadline')
        if deadline and deadline < datetime.date.today():
            raise forms.ValidationError("The deadline cannot be in the past.")
        return deadline
