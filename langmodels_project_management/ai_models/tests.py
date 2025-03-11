from django.test import TestCase, SimpleTestCase
from .models import AIModel
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from project_management.models import Project, ProjectMember, ProjectRole
from ai_documentation.models import AIDocument, DocumentType, DocumentSection
from ai_models.views import TestModellsView, TestGeneratedTextView, SelectProjectView, SelectDocumentView, GenerateView, GenerateSectionContentView, GenerateDescriptionView, GenerateTitleView, ResultsView
from ai_models.forms import TestModelForm, GenerateDescriptionForm, GenerateTitleForm, ProjectSelectionForm, DocumentSelectionForm
from ai_models.services import PipelineTextGenerator, TokenizerModel
AI_MODELS = [
    ("DistilGPT2", "distilbert/distilgpt2"),
    ("GPT-Neo 125M", "EleutherAI/gpt-neo-125m"),
    ("Facebook OPT 125M", "facebook/opt-125m"),
    ("GPT-2 Medium", "openai-community/gpt2-medium"),
    ("Facebook OPT 350M", "facebook/opt-350m"),
]
from django.contrib.admin.sites import site
from ai_models.admin import AIModelAdmin

# ====== models.py ======

class AIModelTestCase(TestCase):
    def setUp(self):
        self.model1 = AIModel.objects.create(name="Model A", model_identifier="model_a")
        self.model2 = AIModel.objects.create(name="Model B", model_identifier="model_b")
    
    def test_model_creation(self):
        self.assertEqual(AIModel.objects.count(), 2)
    
    def test_str_representation(self):
        self.assertEqual(str(self.model1), "Model A (model_a)")
    
    def test_unique_name(self):
        with self.assertRaises(Exception):
            AIModel.objects.create(name="Model A", model_identifier="model_c")
    
    def test_unique_model_identifier(self):
        with self.assertRaises(Exception):
            AIModel.objects.create(name="Model C", model_identifier="model_a")

# ====== views.py ======

class TestModellsViewTests(TestCase):
    def setUp(self):
        self.ai_model = AIModel.objects.create(
            name="Test Model", model_identifier="test-model"
        )
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        self.url = reverse("ai-models:test_models")

    def test_get_request_renders_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ai_models/test_models.html")

class TestGeneratedTextViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        self.url = reverse("ai-models:test_generated_text")

    def test_get_without_session_data_shows_error(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ai_models/test_generated_text.html")
        self.assertContains(response, "No generated text data found.")

    def test_get_with_session_data_displays_generated_text(self):
        session = self.client.session
        session["generated_text_data"] = {
            "prompt": "Test prompt",
            "generated_text": "Generated result",
            "model": "test-model"
        }
        session.save()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ai_models/test_generated_text.html")
        self.assertContains(response, "Test prompt")
        self.assertContains(response, "Generated result")
        self.assertContains(response, "test-model")

    def test_session_data_is_cleared_after_access(self):
        session = self.client.session
        session["generated_text_data"] = {
            "prompt": "Test prompt",
            "generated_text": "Generated result",
            "model": "test-model"
        }
        session.save()

        self.client.get(self.url)
        self.assertNotIn("generated_text_data", self.client.session)

class SelectProjectViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")
        self.staff_user = get_user_model().objects.create_user(username="staffuser", password="testpassword", is_staff=True)
        self.project_owner = get_user_model().objects.create_user(username="owneruser", password="testpassword")
        self.project = Project.objects.create(name="Test Project", owner=self.project_owner)
        self.user_project = Project.objects.create(name="User Project", owner=self.user)
        self.member_project = Project.objects.create(name="Member Project", owner=self.project_owner)

        self.project_role = ProjectRole.objects.create(name="Contributor")
        ProjectMember.objects.create(user=self.user, project=self.member_project, role=self.project_role)

        self.client.login(username="testuser", password="testpassword")
        self.url = reverse("ai-models:select_project")

    def test_access_requires_login(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_get_renders_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ai_models/select_project.html")

    def test_non_staff_user_sees_only_owned_or_member_projects(self):
        response = self.client.get(self.url)
        form = response.context["form"]
        available_projects = list(form.fields["project"].queryset)
        self.assertIn(self.user_project, available_projects)
        self.assertIn(self.member_project, available_projects)
        self.assertNotIn(self.project, available_projects)

    def test_staff_user_sees_all_projects(self):
        self.client.login(username="staffuser", password="testpassword")
        response = self.client.get(self.url)
        form = response.context["form"]
        available_projects = list(form.fields["project"].queryset)
        self.assertIn(self.user_project, available_projects)
        self.assertIn(self.member_project, available_projects)
        self.assertIn(self.project, available_projects)

    def test_form_valid_sets_selected_project_in_session(self):
        response = self.client.post(self.url, {"project": self.user_project.id})
        self.assertRedirects(response, reverse("ai-models:select_document"))
        self.assertEqual(self.client.session["selected_project_id"], self.user_project.id)

    def test_form_invalid_does_not_set_session(self):
        response = self.client.post(self.url, {"project": ""})
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("selected_project_id", self.client.session)

class SelectDocumentViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")
        self.staff_user = get_user_model().objects.create_user(username="staffuser", password="testpassword", is_staff=True)
        self.project_owner = get_user_model().objects.create_user(username="owneruser", password="testpassword")
        self.project = Project.objects.create(name="Test Project", owner=self.project_owner)
        self.user_project = Project.objects.create(name="User Project", owner=self.user)
        self.member_project = Project.objects.create(name="Member Project", owner=self.project_owner)
        
        self.project_role = ProjectRole.objects.create(name="Contributor")
        ProjectMember.objects.create(user=self.user, project=self.member_project, role=self.project_role)

        self.document_type = DocumentType.objects.create(name="Test Type")
        self.ai_model = AIModel.objects.create(name="Test AI Model")

        self.document1 = AIDocument.objects.create(title="Doc1", project=self.project, created_by=self.project_owner, type=self.document_type, ai_model=self.ai_model)
        self.document2 = AIDocument.objects.create(title="Doc2", project=self.user_project, created_by=self.user, type=self.document_type, ai_model=self.ai_model)
        self.document3 = AIDocument.objects.create(title="Doc3", project=self.member_project, created_by=self.project_owner, type=self.document_type, ai_model=self.ai_model)

        self.client.login(username="testuser", password="testpassword")
        self.url = reverse("ai-models:select_document")

    def test_access_requires_login(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_get_without_project_id_in_session_shows_error(self):
        response = self.client.get(self.url, follow=True)
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("The project ID is missing from the session." in msg.message for msg in messages))

    def test_get_with_project_id_in_session_renders_correct_template(self):
        session = self.client.session
        session["selected_project_id"] = self.user_project.id
        session.save()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ai_models/select_document.html")

    def test_non_staff_user_sees_only_own_and_member_documents(self):
        session = self.client.session
        session["selected_project_id"] = self.member_project.id
        session.save()

        response = self.client.get(self.url)
        form = response.context["form"]
        available_documents = list(form.fields["document"].queryset)
        self.assertIn(self.document3, available_documents)
        self.assertNotIn(self.document1, available_documents)
        self.assertNotIn(self.document2, available_documents)

    def test_form_valid_sets_selected_document_in_session(self):
        session = self.client.session
        session["selected_project_id"] = self.user_project.id
        session.save()

        response = self.client.post(self.url, {"document": self.document2.id})
        self.assertRedirects(response, reverse("ai-models:generate"))
        self.assertEqual(self.client.session["selected_document_id"], self.document2.id)

    def test_form_invalid_does_not_set_session(self):
        session = self.client.session
        session["selected_project_id"] = self.user_project.id
        session.save()

        response = self.client.post(self.url, {"document": ""})
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("selected_document_id", self.client.session)

class GenerateViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")
        self.staff_user = get_user_model().objects.create_user(username="staffuser", password="testpassword", is_staff=True)
        self.project_owner = get_user_model().objects.create_user(username="owneruser", password="testpassword")

        self.project = Project.objects.create(name="Test Project", owner=self.project_owner, description="Project Description")
        self.user_project = Project.objects.create(name="User Project", owner=self.user)
        self.member_project = Project.objects.create(name="Member Project", owner=self.project_owner)
        
        self.project_role = ProjectRole.objects.create(name="Contributor")
        ProjectMember.objects.create(user=self.user, project=self.member_project, role=self.project_role)

        self.document_type = DocumentType.objects.create(name="Test Type")
        self.ai_model = AIModel.objects.create(name="Test AI Model")

        self.document1 = AIDocument.objects.create(title="Doc1", content="# Section 1\nText\n---\n# Section 2\nMore text", project=self.project, created_by=self.project_owner, type=self.document_type, ai_model=self.ai_model)
        self.document2 = AIDocument.objects.create(title="Doc2", content="No sections here", project=self.user_project, created_by=self.user, type=self.document_type, ai_model=self.ai_model)

        self.client.login(username="testuser", password="testpassword")
        self.url = reverse("ai-models:generate")

    def test_access_requires_login(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_get_without_document_id_shows_error(self):
        response = self.client.get(self.url, follow=True)
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("The document ID is missing from the session." in msg.message for msg in messages))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ai_models/generate.html")

    def test_get_with_document_id_but_no_permission_redirects(self):
        session = self.client.session
        session["selected_document_id"] = self.document1.id
        session["selected_project_id"] = self.project.id
        session.save()

        response = self.client.get(self.url, follow=True)
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("You do not have permission to access this document." in msg.message for msg in messages))
        self.assertRedirects(response, reverse("ai-models:select_document"))

class GenerateSectionContentViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")
        self.staff_user = get_user_model().objects.create_user(username="staffuser", password="testpassword", is_staff=True)
        self.project_owner = get_user_model().objects.create_user(username="owneruser", password="testpassword")

        self.project = Project.objects.create(name="Test Project", owner=self.project_owner)
        self.user_project = Project.objects.create(name="User Project", owner=self.user)
        self.member_project = Project.objects.create(name="Member Project", owner=self.project_owner)
        
        self.project_role = ProjectRole.objects.create(name="Contributor")
        ProjectMember.objects.create(user=self.user, project=self.member_project, role=self.project_role)

        self.document_type = DocumentType.objects.create(name="Test Type")
        self.ai_model = AIModel.objects.create(name="Test AI Model")

        self.document = AIDocument.objects.create(
            title="Doc1",
            content="# Section 1\nInitial text\n---\n# Section 2\nMore text",
            project=self.project,
            created_by=self.project_owner, 
            type=self.document_type, 
            ai_model=self.ai_model
        )

        self.document_section = DocumentSection.objects.create(
            title="Section 1",
            prompt="Generate content for section 1",
            document_type=self.document.type
        )

        self.client.login(username="testuser", password="testpassword")
        self.url = reverse("ai-models:generate_section_content")

    def test_access_requires_login(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_post_without_permission_redirects(self):
        session = self.client.session
        session["selected_document_id"] = self.document.id
        session["selected_project_id"] = self.project.id
        session.save()

        response = self.client.post(self.url, {
            "section_title": "Section 1",
            "section_content": "Updated content",
            "action": "save"
        }, follow=True)

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("You do not have permission to modify this document." in msg.message for msg in messages))
        self.assertRedirects(response, reverse("ai-models:select_document"))

    def test_post_with_missing_title_or_content_shows_error(self):
        session = self.client.session
        session["selected_document_id"] = self.document.id
        session["selected_project_id"] = self.project.id
        session.save()

        self.project_role = ProjectRole.objects.create(name="Tester")
        ProjectMember.objects.create(user=self.user, project=self.project, role=self.project_role)

        response = self.client.post(self.url, {
            "section_title": "",
            "section_content": "Updated content",
            "action": "save"
        }, follow=True)

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("Missing title or content!" in msg.message for msg in messages))

class GenerateDescriptionViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        self.url = reverse("ai-models:generate_description")
        self.ai_model = AIModel.objects.create(name="Test AI Model", model_identifier="test-model")

    def test_get_renders_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ai_models/generate_description.html")

    def test_invalid_form_submission(self):
        response = self.client.post(self.url, {"title": ""})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")

class GenerateTitleViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        self.url = reverse("ai-models:generate_title")
        self.ai_model = AIModel.objects.create(name="Test AI Model", model_identifier="test-model")

    def test_get_renders_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ai_models/generate_title.html")

    def test_post_valid_data_redirects_to_results(self):
        response = self.client.post(self.url, {"description": "This is a sample project description."})
        self.assertEqual(response.status_code, 200)

class ResultsViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        self.url = reverse("ai-models:results")

    def test_get_without_session_data_shows_error(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ai_models/results.html")
        self.assertContains(response, "No generated text data found.")

    def test_get_with_session_data_displays_results(self):
        session = self.client.session
        session["generated_results"] = {
            "description": "Sample project",
            "results": [
                {"model": "test-model", "generated_text": "AI Generated Title"}
            ]
        }
        session.save()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ai_models/results.html")
        self.assertContains(response, "Sample project")
        self.assertContains(response, "AI Generated Title")

# ====== urls.py ======

class TestAIModelsUrls(SimpleTestCase):
    def test_test_models_url_resolves(self):
        url = reverse("ai-models:test_models")
        self.assertEqual(resolve(url).func.view_class, TestModellsView)

    def test_test_generated_text_url_resolves(self):
        url = reverse("ai-models:test_generated_text")
        self.assertEqual(resolve(url).func.view_class, TestGeneratedTextView)

    def test_select_project_url_resolves(self):
        url = reverse("ai-models:select_project")
        self.assertEqual(resolve(url).func.view_class, SelectProjectView)

    def test_select_document_url_resolves(self):
        url = reverse("ai-models:select_document")
        self.assertEqual(resolve(url).func.view_class, SelectDocumentView)

    def test_generate_url_resolves(self):
        url = reverse("ai-models:generate")
        self.assertEqual(resolve(url).func.view_class, GenerateView)

    def test_generate_section_content_url_resolves(self):
        url = reverse("ai-models:generate_section_content")
        self.assertEqual(resolve(url).func.view_class, GenerateSectionContentView)

    def test_generate_description_url_resolves(self):
        url = reverse("ai-models:generate_description")
        self.assertEqual(resolve(url).func.view_class, GenerateDescriptionView)

    def test_generate_title_url_resolves(self):
        url = reverse("ai-models:generate_title")
        self.assertEqual(resolve(url).func.view_class, GenerateTitleView)

    def test_results_url_resolves(self):
        url = reverse("ai-models:results")
        self.assertEqual(resolve(url).func.view_class, ResultsView)

# ====== forms.py ======

class TestModelFormTests(TestCase):
    def setUp(self):
        self.ai_model = AIModel.objects.create(name="Test AI Model", model_identifier="test-model")

    def test_valid_form(self):
        form = TestModelForm(data={"ai_model": self.ai_model.id, "prompt": "Test prompt"})
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_fields(self):
        form = TestModelForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("ai_model", form.errors)
        self.assertIn("prompt", form.errors)

class GenerateDescriptionFormTests(TestCase):
    def test_valid_form(self):
        form = GenerateDescriptionForm(data={"title": "Sample Project"})
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_title(self):
        form = GenerateDescriptionForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

class GenerateTitleFormTests(TestCase):
    def test_valid_form(self):
        form = GenerateTitleForm(data={"description": "This is a sample description."})
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_description(self):
        form = GenerateTitleForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("description", form.errors)

class ProjectSelectionFormTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")
        self.project = Project.objects.create(name="Test Project", owner=self.user)

    def test_valid_form(self):
        form = ProjectSelectionForm(data={"project": self.project.id}, user=self.user)
        form.fields["project"].queryset = Project.objects.filter(owner=self.user)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_project(self):
        form = ProjectSelectionForm(data={}, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn("project", form.errors)

class DocumentSelectionFormTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")
        self.project = Project.objects.create(name="Test Project", owner=self.user)
        self.document_type = DocumentType.objects.create(name="Test Type")
        self.ai_model = AIModel.objects.create(name="Test AI Model") 
        self.document = AIDocument.objects.create(title="Test Document", project=self.project, created_by=self.user, type=self.document_type, ai_model=self.ai_model)

    def test_valid_form(self):
        form = DocumentSelectionForm(project=self.project, data={"document": self.document.id})
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_document(self):
        form = DocumentSelectionForm(project=self.project, data={})
        self.assertFalse(form.is_valid())
        self.assertIn("document", form.errors)

# ====== services.py ======

class PipelineTextGeneratorTests(TestCase):
    def test_generate_text_returns_string(self):
        prompt = "This is a test prompt."
        for model_name, model_identifier in AI_MODELS:
            with self.subTest(model=model_name):
                generator = PipelineTextGenerator(model_identifier)
                output_text = generator.generate_text(prompt, min_new_tokens=10, max_new_tokens=20)
                self.assertIsInstance(output_text, str)
                self.assertGreater(len(output_text), 0)

    def test_generate_text_with_different_lengths(self):
        prompt = "Test prompt for text generation."
        for model_name, model_identifier in AI_MODELS:
            with self.subTest(model=model_name):
                generator = PipelineTextGenerator(model_identifier)
                output_short = generator.generate_text(prompt, min_new_tokens=5, max_new_tokens=10)
                output_long = generator.generate_text(prompt, min_new_tokens=20, max_new_tokens=50)

                self.assertIsInstance(output_short, str)
                self.assertIsInstance(output_long, str)
                self.assertGreater(len(output_long), len(output_short))

class TokenizerModelTests(TestCase):
    def test_generate_text_returns_string(self):
        prompt = "This is a test prompt."
        for model_name, model_identifier in AI_MODELS:
            with self.subTest(model=model_name):
                tokenizer_model = TokenizerModel(model_identifier)
                output_text = tokenizer_model.generate_text(prompt, min_new_tokens=10, max_new_tokens=20)
                self.assertIsInstance(output_text, str)
                self.assertGreater(len(output_text), 0)

    def test_generate_text_with_different_lengths(self):
        prompt = "Test prompt for text generation."
        for model_name, model_identifier in AI_MODELS:
            with self.subTest(model=model_name):
                tokenizer_model = TokenizerModel(model_identifier)
                output_short = tokenizer_model.generate_text(prompt, min_new_tokens=5, max_new_tokens=10)
                output_long = tokenizer_model.generate_text(prompt, min_new_tokens=20, max_new_tokens=50)

                self.assertIsInstance(output_short, str)
                self.assertIsInstance(output_long, str)
                self.assertGreater(len(output_long), len(output_short))

# ====== admin.py ======

class AIModelAdminTests(TestCase):
    def setUp(self):
        self.admin_site = site
        self.model_admin = AIModelAdmin(AIModel, self.admin_site)

    def test_admin_registered(self):
        self.assertIn(AIModel, self.admin_site._registry)

    def test_list_display(self):
        self.assertEqual(self.model_admin.list_display, ('name', 'model_identifier'))

    def test_search_fields(self):
        self.assertEqual(self.model_admin.search_fields, ('name', 'model_identifier'))

    def test_ordering(self):
        self.assertEqual(self.model_admin.ordering, ('name',))