from django.test import TestCase, Client, SimpleTestCase
from .models import DocumentType, AIDocument, DocumentSection
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from project_management.models import Project, ProjectMember, ProjectRole
from ai_models.models import AIModel
from django.urls import reverse, resolve
from unittest.mock import patch
from pathlib import Path
from django.conf import settings
from utils.clean_filename import clean_filename
import os
import shutil
from ai_documentation.views import (
    DocumentCreateView,
    DocumentListView,
    DocumentDetailView,
    DocumentUpdateView,
    DocumentDeleteView,
    DocumentDownloadView,
)
from ai_documentation.forms import DocumentCreationForm, DocumentUpdateForm
from ai_documentation.admin import (
    DocumentTypeAdmin,
    AIDocumentAdmin,
    DocumentSectionAdmin,
)
from django.contrib.admin.sites import site

# ====== models.py ======


class DocumentTypeModelTest(TestCase):
    def setUp(self):
        self.doc_type = DocumentType.objects.create(name="Test Type")
        self.doc_type_spec, _ = DocumentType.objects.get_or_create(name="Specification")
        self.doc_type_srs, _ = DocumentType.objects.get_or_create(name="SRS")
        self.test_dir = os.path.join(settings.STATICFILES_DIRS[0], "document")

    def test_document_type_creation(self):
        self.assertEqual(str(self.doc_type), "Test Type")
        self.assertEqual(str(self.doc_type_spec), "Specification")
        self.assertEqual(str(self.doc_type_srs), "SRS")

    def test_get_template_file_content_not_found(self):
        content = self.doc_type.get_template_file_content()
        self.assertEqual(content, "Template file not found.")

    def test_get_template_file_content_found_specification(self):
        content = self.doc_type_spec.get_template_file_content().split("\n")[0]
        self.assertEqual(content, "# Project Specification")

    def test_get_template_file_content_found_srs(self):
        content = self.doc_type_srs.get_template_file_content().split("\n")[0]
        self.assertEqual(content, "# Software Requirements Specification (SRS)")


class AIDocumentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser")
        self.project = Project.objects.create(name="Test Project", owner=self.user)
        self.doc_type = DocumentType.objects.create(name="Test Type")
        self.ai_model = AIModel.objects.create(name="Test AI Model")
        self.document = AIDocument.objects.create(
            title="Test Doc",
            content="Test Content",
            project=self.project,
            created_by=self.user,
            type=self.doc_type,
            ai_model=self.ai_model,
        )

    def test_aidocument_creation(self):
        self.assertEqual(
            str(self.document),
            "Test Doc (Project: Test Project (Owner: testuser))",
        )

    def test_version_increment_on_save(self):
        original_version = self.document.version
        self.document.save()
        self.assertEqual(self.document.version, original_version + 1)

    def test_version_not_incremented_on_update(self):
        original_version = self.document.version
        AIDocument.objects.filter(id=self.document.id).update(content="Updated Content")
        updated_document = AIDocument.objects.get(id=self.document.id)
        self.assertEqual(updated_document.version, original_version)

    def test_new_document_initial_version(self):
        new_document = AIDocument(
            title="New Doc",
            content="New Content",
            project=self.project,
            created_by=self.user,
            type=self.doc_type,
            ai_model=self.ai_model,
        )
        new_document.save()
        self.assertEqual(new_document.version, 1)

    def test_created_at_and_updated_at(self):
        self.assertIsNotNone(self.document.created_at)
        self.assertIsNotNone(self.document.updated_at)


class DocumentSectionModelTest(TestCase):
    def setUp(self):
        self.doc_type = DocumentType.objects.create(name="Test Type")
        self.section = DocumentSection.objects.create(
            document_type=self.doc_type, title="Test Section", prompt="Test Prompt"
        )

    def test_document_section_creation(self):
        self.assertEqual(str(self.section), "Test Type - Test Section")

    def test_document_section_dependencies(self):
        section2 = DocumentSection.objects.create(
            document_type=self.doc_type, title="Test Section 2", prompt="Test Prompt 2"
        )
        self.section.dependencies.add(section2)
        self.assertIn(section2, self.section.dependencies.all())


# ====== views.py ======


class DocumentCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser", password="password"
        )
        self.client.login(username="testuser", password="password")

        self.project = Project.objects.create(
            name="Test Project", owner=self.user, description="Test Description"
        )
        project_folder_name = clean_filename(
            f"{self.project.owner.username}_{self.project.name}"
        )
        self.project_folder_path = (
            Path(settings.MEDIA_ROOT) / "projects" / project_folder_name
        )
        os.makedirs(self.project_folder_path, exist_ok=True)

        self.document_type = DocumentType.objects.create(name="Test Type")
        self.ai_model = AIModel.objects.create(name="Test AI Model")

        self.url = reverse("ai-docs:create_document")

    def tearDown(self):
        if self.project_folder_path.exists():
            shutil.rmtree(self.project_folder_path, ignore_errors=True)

    def test_access_requires_login(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_project_queryset_filtered_by_user(self):
        other_user = get_user_model().objects.create_user(
            username="otheruser", password="password"
        )
        Project.objects.create(name="Other Project", owner=other_user)

        response = self.client.get(self.url)
        form = response.context["form"]
        self.assertEqual(list(form.fields["project"].queryset), [self.project])

    @patch("ai_documentation.models.DocumentType.get_template_file_content")
    def test_document_creation_successful(self, mock_get_template):
        mock_get_template.return_value = "Title: {{ document.version }}, Created by: {{ document.created_by.username }}"

        data = {
            "title": "My Test Document",
            "project": self.project.id,
            "type": self.document_type.id,
            "ai_model": self.ai_model.id,
        }

        response = self.client.post(self.url, data, follow=True)
        self.assertEqual(response.status_code, 200)

        document = AIDocument.objects.get(title="My Test Document")
        self.assertEqual(document.created_by, self.user)
        self.assertEqual(document.project, self.project)

        expected_content = "Title: 1, Created by: testuser"
        self.assertEqual(document.content, expected_content)

    @patch("ai_documentation.views.Path.exists", return_value=False)
    def test_error_when_project_folder_does_not_exist(self, mock_path_exists):
        data = {
            "title": "Missing Folder Doc",
            "project": self.project.id,
            "type": self.document_type.id,
            "ai_model": self.ai_model.id,
        }

        response = self.client.post(self.url, data, follow=True)
        self.assertContains(response, "Project folder does not exist", status_code=200)


class DocumentListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser", password="password"
        )
        self.staff_user = get_user_model().objects.create_user(
            username="staffuser", password="password", is_staff=True
        )
        self.other_user = get_user_model().objects.create_user(
            username="otheruser", password="password"
        )

        self.project = Project.objects.create(name="Shared Project", owner=self.user)
        self.project_role = ProjectRole.objects.create(name="Contributor")
        self.document_type = DocumentType.objects.create(name="Test Type")
        self.ai_model = AIModel.objects.create(name="Test AI Model")

        self.own_document = AIDocument.objects.create(
            title="User Document",
            content="Test Content",
            created_by=self.user,
            project=self.project,
            type=self.document_type,
            ai_model=self.ai_model,
        )

        self.other_document = AIDocument.objects.create(
            title="Other Document",
            content="Another Test Content",
            created_by=self.other_user,
            project=self.project,
            type=self.document_type,
            ai_model=self.ai_model,
        )

        ProjectMember.objects.create(
            user=self.user, project=self.project, role=self.project_role
        )

        self.url = reverse("ai-docs:list_documents")

    def test_access_requires_login(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_queryset_for_regular_user(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(self.url)

        documents = list(response.context["documents"])
        self.assertIn(self.own_document, documents)
        self.assertIn(self.other_document, documents)
        self.assertEqual(len(documents), 2)

    def test_queryset_for_staff_user(self):
        self.client.login(username="staffuser", password="password")
        response = self.client.get(self.url)

        documents = list(response.context["documents"])
        self.assertIn(self.own_document, documents)
        self.assertIn(self.other_document, documents)
        self.assertEqual(len(documents), AIDocument.objects.count())

    def test_queryset_for_unrelated_user(self):
        self.client.login(username="otheruser", password="password")
        response = self.client.get(self.url)

        documents = list(response.context["documents"])
        self.assertIn(self.other_document, documents)
        self.assertNotIn(self.own_document, documents)
        self.assertEqual(len(documents), 1)


class DocumentDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser", password="password"
        )
        self.staff_user = get_user_model().objects.create_user(
            username="staffuser", password="password", is_staff=True
        )
        self.other_user = get_user_model().objects.create_user(
            username="otheruser", password="password"
        )

        self.project = Project.objects.create(name="Shared Project", owner=self.user)
        self.project_role = ProjectRole.objects.create(name="Contributor")
        self.document_type = DocumentType.objects.create(name="Test Type")
        self.ai_model = AIModel.objects.create(name="Test AI Model")

        self.document = AIDocument.objects.create(
            title="Test Document",
            content="Sample content",
            created_by=self.user,
            project=self.project,
            type=self.document_type,
            ai_model=self.ai_model,
        )

        ProjectMember.objects.create(
            user=self.user, project=self.project, role=self.project_role
        )

        self.url = reverse("ai-docs:detail_document", kwargs={"pk": self.document.pk})

    def test_access_requires_login(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_document_detail_view_for_owner(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["document"], self.document)
        self.assertTrue(response.context["is_project_member"])

    def test_document_detail_view_for_project_member(self):
        self.client.login(username="otheruser", password="password")
        ProjectMember.objects.create(
            user=self.other_user, project=self.project, role=self.project_role
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["document"], self.document)
        self.assertTrue(response.context["is_project_member"])

    def test_document_detail_view_for_non_member(self):
        self.client.login(username="otheruser", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["document"], self.document)
        self.assertFalse(response.context["is_project_member"])

    def test_document_detail_view_for_staff_user(self):
        self.client.login(username="staffuser", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["document"], self.document)
        self.assertFalse(response.context["is_project_member"])


class DocumentUpdateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser", password="password"
        )
        self.staff_user = get_user_model().objects.create_user(
            username="staffuser", password="password", is_staff=True
        )
        self.other_user = get_user_model().objects.create_user(
            username="otheruser", password="password"
        )

        self.project = Project.objects.create(name="Test Project", owner=self.user)
        project_folder_name = clean_filename(
            f"{self.project.owner.username}_{self.project.name}"
        )
        self.project_folder_path = (
            Path(settings.MEDIA_ROOT) / "projects" / project_folder_name
        )
        os.makedirs(self.project_folder_path, exist_ok=True)
        self.other_project = Project.objects.create(
            name="Other Project", owner=self.user
        )
        self.project_role = ProjectRole.objects.create(name="Contributor")
        self.document_type = DocumentType.objects.create(name="Test Type")
        self.ai_model = AIModel.objects.create(name="Test AI Model")

        self.document = AIDocument.objects.create(
            title="Test Document",
            content="Sample content",
            created_by=self.user,
            project=self.project,
            type=self.document_type,
            ai_model=self.ai_model,
        )

        ProjectMember.objects.create(
            user=self.user, project=self.project, role=self.project_role
        )

        self.url = reverse("ai-docs:update_document", kwargs={"pk": self.document.pk})

    def tearDown(self):
        for project in Project.objects.filter(owner=self.user):
            project_folder_name = clean_filename(
                f"{project.owner.username}_{project.name}"
            )
            project_folder_path = (
                Path(settings.MEDIA_ROOT) / "projects" / project_folder_name
            )
            if project_folder_path.exists():
                shutil.rmtree(project_folder_path, ignore_errors=True)

    def test_access_requires_login(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_update_document_view_for_owner(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["document"], self.document)

    def test_update_document_view_for_staff_user(self):
        self.client.login(username="staffuser", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["document"], self.document)

    def test_update_document_view_for_non_member(self):
        self.client.login(username="otheruser", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)

    def test_successful_document_update(self):
        self.client.login(username="testuser", password="password")
        new_data = {
            "title": "Updated Document",
            "content": "Updated content",
            "project": self.project.id,
            "type": self.document_type.id,
            "ai_model": self.ai_model.id,
        }

        response = self.client.post(self.url, new_data, follow=True)
        self.assertEqual(response.status_code, 200)

        updated_document = AIDocument.objects.get(pk=self.document.pk)
        self.assertEqual(updated_document.title, "Updated Document")
        self.assertEqual(updated_document.content, "Updated content")


class DocumentDeleteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser", password="password"
        )
        self.staff_user = get_user_model().objects.create_user(
            username="staffuser", password="password", is_staff=True
        )
        self.other_user = get_user_model().objects.create_user(
            username="otheruser", password="password"
        )

        self.project = Project.objects.create(name="Test Project", owner=self.user)
        self.project_role = ProjectRole.objects.create(name="Contributor")
        self.document_type = DocumentType.objects.create(name="Test Type")
        self.ai_model = AIModel.objects.create(name="Test AI Model")

        project_folder_name = clean_filename(
            f"{self.project.owner.username}_{self.project.name}"
        )
        self.project_folder_path = (
            Path(settings.MEDIA_ROOT) / "projects" / project_folder_name
        )
        os.makedirs(self.project_folder_path, exist_ok=True)

        self.document = AIDocument.objects.create(
            title="Test Document",
            content="Sample content",
            created_by=self.user,
            project=self.project,
            type=self.document_type,
            ai_model=self.ai_model,
        )

        ProjectMember.objects.create(
            user=self.user, project=self.project, role=self.project_role
        )

        self.url = reverse("ai-docs:delete_document", kwargs={"pk": self.document.pk})

    def tearDown(self):
        if self.project_folder_path.exists():
            shutil.rmtree(self.project_folder_path, ignore_errors=True)

    def test_access_requires_login(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_document_delete_view_for_owner(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["document"], self.document)

    def test_document_delete_view_for_staff_user(self):
        self.client.login(username="staffuser", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["document"], self.document)

    def test_document_delete_view_for_non_member(self):
        self.client.login(username="otheruser", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)

    @patch("pathlib.Path.unlink")
    def test_successful_document_deletion(self, mock_unlink):
        self.client.login(username="testuser", password="password")

        file_path = self.project_folder_path / "test_document.md"
        file_path.touch()

        response = self.client.post(self.url, follow=True)
        self.assertEqual(response.status_code, 200)

        with self.assertRaises(AIDocument.DoesNotExist):
            AIDocument.objects.get(pk=self.document.pk)

        mock_unlink.assert_called_once()

    def test_document_deletion_file_not_found(self):
        self.client.login(username="testuser", password="password")

        response = self.client.post(self.url, follow=True)
        self.assertEqual(response.status_code, 200)

        with self.assertRaises(AIDocument.DoesNotExist):
            AIDocument.objects.get(pk=self.document.pk)


class DocumentDownloadViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser", password="password"
        )
        self.staff_user = get_user_model().objects.create_user(
            username="staffuser", password="password", is_staff=True
        )
        self.other_user = get_user_model().objects.create_user(
            username="otheruser", password="password"
        )

        self.project = Project.objects.create(name="Test Project", owner=self.user)
        self.project_role = ProjectRole.objects.create(name="Contributor")
        self.document_type = DocumentType.objects.create(name="Test Type")
        self.ai_model = AIModel.objects.create(name="Test AI Model")

        self.document = AIDocument.objects.create(
            title="Test Document",
            content="Sample content",
            created_by=self.user,
            project=self.project,
            type=self.document_type,
            ai_model=self.ai_model,
        )

        ProjectMember.objects.create(
            user=self.user, project=self.project, role=self.project_role
        )

        self.url = reverse("ai-docs:download_document", kwargs={"pk": self.document.pk})

        project_folder_name = clean_filename(
            f"{self.project.owner.username}_{self.project.name}"
        )
        self.project_folder_path = (
            Path(settings.MEDIA_ROOT) / "projects" / project_folder_name
        )
        self.document_filename = clean_filename(self.document.title) + ".md"
        self.document_file_path = self.project_folder_path / self.document_filename

        self.project_folder_path.mkdir(parents=True, exist_ok=True)
        with open(self.document_file_path, "w") as f:
            f.write("Test file content")

    def tearDown(self):
        if self.project_folder_path.exists():
            shutil.rmtree(self.project_folder_path, ignore_errors=True)

    def test_access_requires_login(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_download_document_for_owner(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response["Content-Disposition"],
            f'attachment; filename="{clean_filename(self.document.title)}.md"',
        )

    def test_download_document_for_staff(self):
        self.client.login(username="staffuser", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response["Content-Disposition"],
            f'attachment; filename="{clean_filename(self.document.title)}.md"',
        )

    def test_download_document_for_project_member(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_download_document_for_non_member(self):
        self.client.login(username="otheruser", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)

    def test_download_nonexistent_document_as_other_user(self):
        self.client.login(username="otheruser", password="password")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)


# ====== urls.py ======


class TestAIDocumentUrls(SimpleTestCase):
    def test_create_document_url_resolves(self):
        url = reverse("ai-docs:create_document")
        self.assertEqual(resolve(url).func.view_class, DocumentCreateView)

    def test_list_documents_url_resolves(self):
        url = reverse("ai-docs:list_documents")
        self.assertEqual(resolve(url).func.view_class, DocumentListView)

    def test_detail_document_url_resolves(self):
        url = reverse("ai-docs:detail_document", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, DocumentDetailView)

    def test_update_document_url_resolves(self):
        url = reverse("ai-docs:update_document", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, DocumentUpdateView)

    def test_delete_document_url_resolves(self):
        url = reverse("ai-docs:delete_document", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, DocumentDeleteView)

    def test_download_document_url_resolves(self):
        url = reverse("ai-docs:download_document", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, DocumentDownloadView)


# ====== forms.py ======


class DocumentCreationFormTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="password"
        )
        self.project = Project.objects.create(name="Test Project", owner=self.user)
        self.document_type = DocumentType.objects.create(name="Test Type")
        self.ai_model = AIModel.objects.create(name="Test AI Model")

    def test_valid_form(self):
        form_data = {
            "title": "Test Document",
            "content": "Sample content",
            "project": self.project.id,
            "type": self.document_type.id,
            "ai_model": self.ai_model.id,
        }
        form = DocumentCreationForm(data=form_data, user=self.user)
        form.fields["project"].queryset = Project.objects.filter(owner=self.user)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_fields(self):
        form_data = {
            "title": "",
            "content": "",
            "project": "",
            "type": "",
            "ai_model": "",
        }
        form = DocumentCreationForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)
        self.assertIn("project", form.errors)
        self.assertIn("type", form.errors)
        self.assertIn("ai_model", form.errors)

    def test_form_saves_document_with_correct_user(self):
        form_data = {
            "title": "Test Document",
            "content": "Sample content",
            "project": self.project.id,
            "type": self.document_type.id,
            "ai_model": self.ai_model.id,
        }
        form = DocumentCreationForm(data=form_data, user=self.user)
        form.fields["project"].queryset = Project.objects.filter(owner=self.user)
        if form.is_valid():
            document = form.save()
            self.assertEqual(document.created_by, self.user)
            self.assertEqual(document.title, "Test Document")


class DocumentUpdateFormTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="password"
        )
        self.project = Project.objects.create(name="Test Project", owner=self.user)
        self.document_type = DocumentType.objects.create(name="Test Type")
        self.ai_model = AIModel.objects.create(name="Test AI Model")
        self.document = AIDocument.objects.create(
            title="Original Title",
            content="Original Content",
            created_by=self.user,
            project=self.project,
            type=self.document_type,
            ai_model=self.ai_model,
        )

    def test_valid_update_form(self):
        form_data = {
            "title": "Updated Title",
            "content": "Updated Content",
            "project": self.project.id,
            "type": self.document_type.id,
            "ai_model": self.ai_model.id,
        }
        form = DocumentUpdateForm(instance=self.document, data=form_data)
        form.fields["project"].queryset = Project.objects.filter(owner=self.user)
        self.assertTrue(form.is_valid())

    def test_invalid_update_form_missing_required_fields(self):
        form_data = {
            "title": "",
            "content": "Updated Content",
            "project": "",
            "type": "",
            "ai_model": "",
        }
        form = DocumentUpdateForm(instance=self.document, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)
        self.assertIn("project", form.errors)
        self.assertIn("ai_model", form.errors)

    def test_update_form_disables_type_field(self):
        form = DocumentUpdateForm(instance=self.document)
        self.assertTrue(form.fields["type"].widget.attrs.get("disabled"))

    def test_update_form_saves_correctly(self):
        form_data = {
            "title": "Updated Title",
            "content": "Updated Content",
            "project": self.project.id,
            "type": self.document_type.id,
            "ai_model": self.ai_model.id,
        }
        form = DocumentUpdateForm(instance=self.document, data=form_data)
        form.fields["project"].queryset = Project.objects.filter(owner=self.user)
        if form.is_valid():
            updated_document = form.save()
            self.assertEqual(updated_document.title, "Updated Title")
            self.assertEqual(updated_document.content, "Updated Content")


# ====== admin.py ======


class AdminSiteTest(TestCase):
    def test_document_type_admin_registered(self):
        self.assertTrue(site.is_registered(DocumentType))
        self.assertIsInstance(site._registry[DocumentType], DocumentTypeAdmin)

    def test_ai_document_admin_registered(self):
        self.assertTrue(site.is_registered(AIDocument))
        self.assertIsInstance(site._registry[AIDocument], AIDocumentAdmin)

    def test_document_section_admin_registered(self):
        self.assertTrue(site.is_registered(DocumentSection))
        self.assertIsInstance(site._registry[DocumentSection], DocumentSectionAdmin)

    def test_document_type_admin_list_display(self):
        admin_instance = DocumentTypeAdmin(DocumentType, site)
        self.assertEqual(admin_instance.list_display, ("name",))

    def test_document_type_admin_search_fields(self):
        admin_instance = DocumentTypeAdmin(DocumentType, site)
        self.assertEqual(admin_instance.search_fields, ("name",))

    def test_ai_document_admin_list_display(self):
        admin_instance = AIDocumentAdmin(AIDocument, site)
        self.assertEqual(
            admin_instance.list_display,
            (
                "title",
                "project",
                "created_by",
                "created_at",
                "updated_at",
                "version",
                "type",
                "ai_model",
            ),
        )

    def test_ai_document_admin_search_fields(self):
        admin_instance = AIDocumentAdmin(AIDocument, site)
        self.assertEqual(
            admin_instance.search_fields,
            ("title", "project__name", "created_by__username"),
        )

    def test_ai_document_admin_list_filter(self):
        admin_instance = AIDocumentAdmin(AIDocument, site)
        self.assertEqual(
            admin_instance.list_filter, ("project", "created_by", "type", "ai_model")
        )

    def test_document_section_admin_list_display(self):
        admin_instance = DocumentSectionAdmin(DocumentSection, site)
        self.assertEqual(admin_instance.list_display, ("document_type", "title"))

    def test_document_section_admin_search_fields(self):
        admin_instance = DocumentSectionAdmin(DocumentSection, site)
        self.assertEqual(admin_instance.search_fields, ("title", "document_type__name"))

    def test_document_section_admin_filter_horizontal(self):
        admin_instance = DocumentSectionAdmin(DocumentSection, site)
        self.assertEqual(admin_instance.filter_horizontal, ("dependencies",))
