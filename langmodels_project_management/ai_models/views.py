from django.shortcuts import render, redirect
from .services import BaseModel
from .forms import TestModelForm
from django.views.generic import FormView, TemplateView
from django.contrib import messages
from django.urls import reverse

class TestModellsView(FormView):
    template_name="ai_models/test_models.html"
    form_class = TestModelForm

    def form_valid(self, form):
        ai_model = form.cleaned_data["ai_model"]
        prompt = form.cleaned_data["prompt"]
        model_identifier = ai_model.model_identifier

        try:
            ai_model_instance = BaseModel(model_identifier)
            generated_text = ai_model_instance.generate_text(prompt=prompt)

        except Exception as e:
            messages.error(self.request, f"Error while generating text: {str(e)}")
            return self.form_invalid(form)

        self.request.session["generated_text_data"] = {
            "prompt": prompt,
            "generated_text": generated_text,
            "model": model_identifier,
        }

        messages.success(self.request, "Text generated successfully!")
        return redirect(reverse("ai-models:test_generated_test"))

class TestGeneratedTextView(TemplateView):
    template_name = "ai_models/test_generated_text.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.request.session.pop("generated_text_data", None)
        if not data:
            context["error"] = "No generated text data found."
        else:
            context.update(data)
        return context