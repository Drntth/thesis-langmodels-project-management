import uuid
from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from project_management.models import Project, ProjectStatus
from ai_documentation.models import AIDocument, DocumentType
from ai_models.models import AIModel
from .views import HomePageView

# ====== views.py ======


class HomePageViewTest(TestCase):
    def setUp(self):
        self.initial_project_count = Project.objects.count()
        self.initial_ai_document_count = AIDocument.objects.count()
        self.initial_user_count = User.objects.count()

        self.user1 = User.objects.create_user(
            username="testuser1", password="testPass123"
        )
        self.user2 = User.objects.create_user(
            username="testuser2", password="testPass123"
        )

        self.status, _ = ProjectStatus.objects.get_or_create(name="Draft")

        suffix = str(uuid.uuid4())[:8]

        self.project1 = Project.objects.create(
            name=f"Project Alpha {suffix}",
            description="First test project",
            owner=self.user1,
            status=self.status,
        )
        self.project2 = Project.objects.create(
            name=f"Project Beta {suffix}",
            description="Second test project",
            owner=self.user2,
            status=self.status,
        )
        self.project3 = Project.objects.create(
            name=f"Project Gamma {suffix}",
            description="Third test project",
            owner=self.user1,
            status=self.status,
        )
        self.project4 = Project.objects.create(
            name=f"Project Delta {suffix}",
            description="Excluded project",
            owner=self.user1,
            status=self.status,
        )

        self.document_type = DocumentType.objects.create(name=f"Specs {suffix}")
        self.ai_model = AIModel.objects.create(
            name=f"Test AI Model {suffix}", model_identifier=f"test-ai-model-{suffix}"
        )

        self.ai_document1 = AIDocument.objects.create(
            title=f"Test Document 1 {suffix}",
            content="This is a test document.",
            project=self.project1,
            created_by=self.user1,
            type=self.document_type,
            ai_model=self.ai_model,
        )
        self.ai_document = AIDocument.objects.create(
            title=f"Test Document 2 {suffix}",
            content="This is a test document.",
            project=self.project2,
            created_by=self.user2,
            type=self.document_type,
            ai_model=self.ai_model,
        )

        self.url = reverse("home:index")

    def test_homepage_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "home/index.html")

    def test_homepage_context_contains_projects(self):
        response = self.client.get(self.url)
        self.assertIn("projects", response.context)
        project_names = [project.name for project in response.context["projects"]]
        self.assertListEqual(
            sorted(project_names), ["Project Alpha", "Project Beta", "Project Gamma"]
        )

    def test_homepage_context_contains_project_count(self):
        response = self.client.get(self.url)
        self.assertEqual(
            response.context["project_count"], self.initial_project_count + 4
        )

    def test_homepage_context_contains_ai_document_count(self):
        response = self.client.get(self.url)
        self.assertEqual(
            response.context["ai_document_count"], self.initial_ai_document_count + 2
        )

    def test_homepage_context_contains_user_count(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context["user_count"], self.initial_user_count + 2)


# ====== urls.py ======


class TestHomeUrls(TestCase):
    def test_home_url_resolves(self):
        url = reverse("home:index")
        self.assertEqual(resolve(url).func.view_class, HomePageView)

    def test_home_url_status_code(self):
        response = self.client.get(reverse("home:index"))
        self.assertEqual(response.status_code, 200)
