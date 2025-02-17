from django import forms
from .models import AIModel

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