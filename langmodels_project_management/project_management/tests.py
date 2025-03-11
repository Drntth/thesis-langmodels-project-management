from django.test import TestCase, Client
from .models import ProjectStatus, Project,  ProjectRole, ProjectMember
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from utils.clean_filename import clean_filename
from pathlib import Path
from django.conf import settings
import shutil
from unittest.mock import patch
from .views import ProjectCreateView, ProjectListView, ProjectDetailView, ProjectUpdateView, ProjectDeleteView, ProjectMemberCreateView, ProjectMemberRemoveView
import datetime
from .forms import ProjectCreationForm, ProjectUpdateForm, ProjectMemberForm
from django.contrib.admin.sites import site
from .admin import ProjectAdmin, ProjectStatusAdmin, ProjectRoleAdmin, ProjectMemberAdmin

# ====== models.py ======

class ProjectStatusModelTest(TestCase):
    def setUp(self):
        self.project_status = ProjectStatus.objects.create(name="In Progress")

    def test_project_status_creation(self):
        self.assertEqual(self.project_status.name, "In Progress")
        self.assertEqual(str(self.project_status), "In Progress")
    
    def test_unique_project_status_name(self):
        with self.assertRaises(Exception):
            ProjectStatus.objects.create(name="In Progress")

class ProjectModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testPass123')
        self.status = ProjectStatus.objects.create(name="In Progress")
        self.project = Project.objects.create(name="Test Project", owner=self.user, status=self.status)

    def test_project_creation(self):
        self.assertEqual(self.project.name, "Test Project")
        self.assertEqual(self.project.owner.username, "testuser")
        self.assertEqual(self.project.status.name, "In Progress")

    def test_project_status_default(self):
        project_without_status = Project.objects.create(name="Draft Test Project", owner=self.user)
        self.assertEqual(project_without_status.status.name, "Draft")

    def test_project_str_method(self):
        self.assertEqual(str(self.project), "Test Project (Owner: testuser)")

    def test_project_name_unique(self):
        with self.assertRaises(Exception):
            Project.objects.create(name="Test Project", owner=self.user, status=self.status)

class ProjectRoleModelTest(TestCase):
    def setUp(self):
        self.project_role = ProjectRole.objects.create(name="Manager")

    def test_project_role_creation(self):
        self.assertEqual(self.project_role.name, "Manager")
        self.assertEqual(str(self.project_role), "Manager")

    def test_unique_project_role_name(self):
        with self.assertRaises(Exception):
            ProjectRole.objects.create(name="Manager")

class ProjectMemberModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testPass123')
        self.project = Project.objects.create(name="Test Project", owner=self.user)
        self.role = ProjectRole.objects.create(name="Developer")
        self.project_member = ProjectMember.objects.create(user=self.user, project=self.project, role=self.role)

    def test_project_member_creation(self):
        self.assertEqual(self.project_member.user.username, "testuser")
        self.assertEqual(self.project_member.project.name, "Test Project")
        self.assertEqual(self.project_member.role.name, "Developer")
        self.assertEqual(str(self.project_member), "testuser - Developer in Test Project")

    def test_unique_together_constraint(self):
        with self.assertRaises(Exception):
            ProjectMember.objects.create(user=self.user, project=self.project, role=self.role)

    def test_project_status_update_on_member_addition(self):
        project_with_member = Project.objects.create(name="New Project", owner=self.user)
        member = ProjectMember.objects.create(user=self.user, project=project_with_member, role=self.role)
        self.assertEqual(project_with_member.status.name, "In Progress")

# ====== views.py ======

class ProjectCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username="testuser", password="testPass123")
        self.client.login(username="testuser", password="testPass123")

        self.project_data = {
            'name': 'Test Project',
            'description': 'This is a test project.'
        }

        self.url = reverse('projects:create_project')

    def tearDown(self):
        project_folder_name = clean_filename(f"{self.user.username}_{self.project_data['name']}")
        project_folder_path = Path(settings.MEDIA_ROOT) / "projects" / project_folder_name
        if project_folder_path.exists():
            shutil.rmtree(project_folder_path)

    def test_access_requires_login(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_project_create_view_get(self):
        response = self.client.get(reverse("projects:create_project"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project_management/create_project.html")

    def test_project_creation(self):
        response = self.client.post(reverse('projects:create_project'), data=self.project_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Project.objects.filter(name='Test Project', owner=self.user).exists())

    def test_project_folder_creation(self):
        self.client.post(reverse('projects:create_project'), data=self.project_data, follow=True)
        project_folder_name = clean_filename(f"{self.user.username}_{self.project_data['name']}")
        project_folder_path = Path(settings.MEDIA_ROOT) / "projects" / project_folder_name
        self.assertTrue(project_folder_path.exists())

class ProjectListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.owner = get_user_model().objects.create_user(username='owner', password='testPass123')
        self.member = get_user_model().objects.create_user(username='member', password='testPass123')
        self.staff_user = get_user_model().objects.create_superuser(username='staff', password='testPass123', is_staff=True)

        self.project = Project.objects.create(name='Test Project', owner=self.owner)

        self.project_role = ProjectRole.objects.create(name="Contributor")
        ProjectMember.objects.create(user=self.member, project=self.project, role=self.project_role)

        self.url = reverse('projects:list_projects')

    def test_access_requires_login(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_owner_sees_own_project(self):
        self.client.login(username='owner', password='testPass123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.project, response.context['projects'])

    def test_member_sees_assigned_project(self):
        self.client.login(username='member', password='testPass123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.project, response.context['projects'])

    def test_staff_sees_all_projects(self):
        self.client.login(username='staff', password='testPass123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.project, response.context['projects'])

class ProjectDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.owner = get_user_model().objects.create_user(username='owner', password='testPass123')
        self.member = get_user_model().objects.create_user(username='member', password='testPass123')

        self.project = Project.objects.create(name='Test Project', owner=self.owner)

        self.project_role = ProjectRole.objects.create(name="Contributor")
        ProjectMember.objects.create(user=self.member, project=self.project, role=self.project_role)

        self.url = reverse('projects:detail_project', kwargs={'pk': self.project.pk})

    def test_access_requires_login(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_owner_can_view_project(self):
        self.client.login(username='owner', password='testPass123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['project'], self.project)

    def test_member_can_view_project(self):
        self.client.login(username='member', password='testPass123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['project'], self.project)
        self.assertTrue(response.context['is_project_member'])

class ProjectUpdateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.owner = get_user_model().objects.create_user(username='owner', password='testPass123')
        self.member = get_user_model().objects.create_user(username='member', password='testPass123')
        self.staff_user = get_user_model().objects.create_superuser(username='staff', password='testPass123', is_staff=True)

        self.project = Project.objects.create(name='Test Project', owner=self.owner)

        self.project_role = ProjectRole.objects.create(name="Contributor")
        ProjectMember.objects.create(user=self.member, project=self.project, role=self.project_role)

        self.url = reverse('projects:update_project', kwargs={'pk': self.project.pk})

    def tearDown(self):
        project_folder_name1 = clean_filename(f"{self.owner.username}_test_project")
        project_folder_path1 = Path(settings.MEDIA_ROOT) / "projects" / project_folder_name1
        if project_folder_path1.exists():
            shutil.rmtree(project_folder_path1)

        project_folder_name2 = clean_filename(f"{self.owner.username}_updated_project")
        project_folder_path2 = Path(settings.MEDIA_ROOT) / "projects" / project_folder_name2
        if project_folder_path2.exists():
            shutil.rmtree(project_folder_path2)

    def test_access_requires_login(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_owner_can_access_update_page(self):
        self.client.login(username='owner', password='testPass123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_management/update_project.html')

    def test_member_can_access_update_page(self):
        self.client.login(username='member', password='testPass123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_management/update_project.html')

    def test_staff_can_access_update_page(self):
        self.client.login(username='staff', password='testPass123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_management/update_project.html')

class ProjectDeleteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.owner = get_user_model().objects.create_user(username='owner', password='testPass123')
        self.member = get_user_model().objects.create_user(username='member', password='testPass123')
        self.staff_user = get_user_model().objects.create_superuser(username='staff', password='testPass123', is_staff=True)

        self.project = Project.objects.create(name='Test Project', owner=self.owner)

        self.project_role = ProjectRole.objects.create(name="Contributor")
        ProjectMember.objects.create(user=self.member, project=self.project, role=self.project_role)

        self.project_folder_path = Path(settings.MEDIA_ROOT) / "projects" / f"{self.project.owner.username}_{self.project.name}"
        self.project_folder_path.mkdir(parents=True, exist_ok=True)

        self.url = reverse('projects:delete_project', kwargs={'pk': self.project.pk})

    def tearDown(self):
        if self.project_folder_path.exists():
            shutil.rmtree(self.project_folder_path, ignore_errors=True)

    def test_access_requires_login(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_owner_can_access_delete_page(self):
        self.client.login(username='owner', password='testPass123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_management/delete_project.html')

    def test_member_can_access_delete_page(self):
        self.client.login(username='member', password='testPass123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_management/delete_project.html')

    def test_staff_can_access_delete_page(self):
        self.client.login(username='staff', password='testPass123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_management/delete_project.html')

    def test_successful_project_deletion(self):
        self.client.login(username='owner', password='testPass123')
        response = self.client.post(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Project.objects.filter(pk=self.project.pk).exists())

    def test_project_deletion_folder_not_found(self):
        self.client.login(username='owner', password='testPass123')
        shutil.rmtree(self.project_folder_path, ignore_errors=True)
        response = self.client.post(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Project.objects.filter(pk=self.project.pk).exists())

class ProjectMemberCreateViewTest(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username='owner', password='testPass123')
        self.new_member = User.objects.create_user(username='newmember', password='testPass123')
        self.project = Project.objects.create(name='Test Project', owner=self.owner)
        self.url = reverse('projects:add_member', kwargs={'pk': self.project.pk})

    def test_access_requires_login(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_owner_can_access_add_member_page(self):
        self.client.login(username='owner', password='testPass123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_management/add_member.html')

class ProjectMemberRemoveViewTest(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username='owner', password='testPass123')
        self.member = User.objects.create_user(username='member', password='testPass123')
        self.staff_user = User.objects.create_superuser(username='staff', password='testPass123')
        self.project = Project.objects.create(name='Test Project', owner=self.owner)
        self.project_role = ProjectRole.objects.create(name="Contributor")
        self.project_member = ProjectMember.objects.create(project=self.project, user=self.member, role=self.project_role)

        self.url = reverse('projects:remove_member', kwargs={'pk': self.project_member.pk})

    def test_access_requires_login(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_owner_can_remove_member(self):
        self.client.login(username='owner', password='testPass123')
        response = self.client.post(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(ProjectMember.objects.filter(pk=self.project_member.pk).exists())

    def test_staff_can_remove_member(self):
        self.client.login(username='staff', password='testPass123')
        response = self.client.post(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(ProjectMember.objects.filter(pk=self.project_member.pk).exists())

# ====== urls.py ======

class TestProjectURLs(TestCase):
    def test_create_project_url_resolves(self):
        url = reverse('projects:create_project')
        self.assertEqual(resolve(url).func.view_class, ProjectCreateView)

    def test_create_project_url_status_code(self):
        response = self.client.get(reverse('projects:create_project'))
        self.assertIn(response.status_code, [200, 302])

    def test_list_projects_url_resolves(self):
        url = reverse('projects:list_projects')
        self.assertEqual(resolve(url).func.view_class, ProjectListView)

    def test_list_projects_url_status_code(self):
        response = self.client.get(reverse('projects:list_projects'))
        self.assertIn(response.status_code, [200, 302])

    def test_detail_project_url_resolves(self):
        url = reverse('projects:detail_project', args=[1])
        self.assertEqual(resolve(url).func.view_class, ProjectDetailView)

    def test_detail_project_url_status_code(self):
        response = self.client.get(reverse('projects:detail_project', args=[1]))
        self.assertIn(response.status_code, [200, 302])

    def test_update_project_url_resolves(self):
        url = reverse('projects:update_project', args=[1])
        self.assertEqual(resolve(url).func.view_class, ProjectUpdateView)

    def test_update_project_url_status_code(self):
        response = self.client.get(reverse('projects:update_project', args=[1]))
        self.assertIn(response.status_code, [200, 302])

    def test_delete_project_url_resolves(self):
        url = reverse('projects:delete_project', args=[1])
        self.assertEqual(resolve(url).func.view_class, ProjectDeleteView)

    def test_delete_project_url_status_code(self):
        response = self.client.get(reverse('projects:delete_project', args=[1]))
        self.assertIn(response.status_code, [200, 302])

    def test_add_member_url_resolves(self):
        url = reverse('projects:add_member', args=[1])
        self.assertEqual(resolve(url).func.view_class, ProjectMemberCreateView)

    def test_add_member_url_status_code(self):
        response = self.client.get(reverse('projects:add_member', args=[1]))
        self.assertIn(response.status_code, [200, 302])

    def test_remove_member_url_resolves(self):
        url = reverse('projects:remove_member', args=[1])
        self.assertEqual(resolve(url).func.view_class, ProjectMemberRemoveView)

# ====== forms.py ======

class ProjectCreationFormTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testPass123')

    def test_valid_form(self):
        form_data = {
            'name': 'Test Project',
            'description': 'A sample project.',
            'deadline': (datetime.date.today() + datetime.timedelta(days=10)).strftime('%Y-%m-%d')
        }
        form = ProjectCreationForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())

    def test_missing_name(self):
        form_data = {
            'description': 'A sample project.',
            'deadline': (datetime.date.today() + datetime.timedelta(days=10)).strftime('%Y-%m-%d')
        }
        form = ProjectCreationForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_deadline_in_past(self):
        form_data = {
            'name': 'Test Project',
            'description': 'A sample project.',
            'deadline': (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        }
        form = ProjectCreationForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('deadline', form.errors)

    def test_save_form_sets_owner(self):
        form_data = {
            'name': 'Test Project',
            'description': 'A sample project.',
            'deadline': (datetime.date.today() + datetime.timedelta(days=10)).strftime('%Y-%m-%d')
        }
        form = ProjectCreationForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())
        project = form.save(commit=False)
        self.assertEqual(project.owner, self.user)

class ProjectUpdateFormTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testPass123')
        self.status = ProjectStatus.objects.create(name='In Progress')
        self.project = Project.objects.create(name='Old Name', description='Old Desc', deadline=datetime.date.today(), status=self.status, owner_id=self.user.id)

    def test_valid_update_form(self):
        form_data = {
            'name': 'Updated Project',
            'description': 'Updated Description',
            'deadline': (datetime.date.today() + datetime.timedelta(days=5)).strftime('%Y-%m-%d'),
            'status': self.status.id
        }
        form = ProjectUpdateForm(data=form_data, instance=self.project)
        self.assertTrue(form.is_valid())

    def test_invalid_past_deadline(self):
        form_data = {
            'name': 'Updated Project',
            'description': 'Updated Description',
            'deadline': (datetime.date.today() - datetime.timedelta(days=5)).strftime('%Y-%m-%d'),
            'status': self.status.id
        }
        form = ProjectUpdateForm(data=form_data, instance=self.project)
        self.assertFalse(form.is_valid())
        self.assertIn('deadline', form.errors)

class ProjectMemberFormTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testPass123')
        self.project = Project.objects.create(name='Test Project', owner_id=self.user.id)
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.role = ProjectRole.objects.create(name='Developer')
        ProjectMember.objects.create(project=self.project, user=self.user1, role=self.role)

    def test_valid_member_form(self):
        form_data = {
            'user': self.user2.id,
            'role': self.role.id
        }
        form = ProjectMemberForm(data=form_data, project=self.project)
        self.assertTrue(form.is_valid())

    def test_existing_member_exclusion(self):
        form = ProjectMemberForm(project=self.project)
        self.assertNotIn(self.user1, form.fields['user'].queryset)

# ====== admin.py ======

class AdminSiteTest(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpassword')
        self.client.login(username='admin', password='adminpassword')
        self.project_status = ProjectStatus.objects.create(name='Active')
        self.project_role = ProjectRole.objects.create(name='Developer')
        self.user = User.objects.create_user(username='testuser', password='password')
        self.project = Project.objects.create(name='Test Project', owner=self.user, status=self.project_status)
        self.project_member = ProjectMember.objects.create(user=self.user, project=self.project, role=self.project_role)

    def test_project_status_admin_registered(self):
        self.assertTrue(site.is_registered(ProjectStatus))
        self.assertIsInstance(site._registry[ProjectStatus], ProjectStatusAdmin)

    def test_project_admin_registered(self):
        self.assertTrue(site.is_registered(Project))
        self.assertIsInstance(site._registry[Project], ProjectAdmin)

    def test_project_role_admin_registered(self):
        self.assertTrue(site.is_registered(ProjectRole))
        self.assertIsInstance(site._registry[ProjectRole], ProjectRoleAdmin)

    def test_project_member_admin_registered(self):
        self.assertTrue(site.is_registered(ProjectMember))
        self.assertIsInstance(site._registry[ProjectMember], ProjectMemberAdmin)

    def test_project_admin_list_display(self):
        admin_instance = ProjectAdmin(Project, site)
        self.assertEqual(admin_instance.list_display, ('name', 'owner', 'status', 'deadline', 'created_at'))

    def test_project_admin_search_fields(self):
        admin_instance = ProjectAdmin(Project, site)
        self.assertEqual(admin_instance.search_fields, ('name', 'owner__username'))

    def test_project_admin_list_filter(self):
        admin_instance = ProjectAdmin(Project, site)
        self.assertEqual(admin_instance.list_filter, ('status', 'created_at'))

    def test_project_member_admin_list_display(self):
        admin_instance = ProjectMemberAdmin(ProjectMember, site)
        self.assertEqual(admin_instance.list_display, ('user', 'project', 'role'))

    def test_project_member_admin_search_fields(self):
        admin_instance = ProjectMemberAdmin(ProjectMember, site)
        self.assertEqual(admin_instance.search_fields, ('user__username', 'project__name'))

    def test_project_member_admin_list_filter(self):
        admin_instance = ProjectMemberAdmin(ProjectMember, site)
        self.assertEqual(admin_instance.list_filter, ('role', 'project'))