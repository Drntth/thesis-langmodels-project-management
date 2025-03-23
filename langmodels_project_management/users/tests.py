from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from django.contrib.messages import get_messages
from .views import (
    ProfileDetailView,
    ProfileUpdateView,
    CustomPasswordChangeView,
    ProfileDeleteView,
)
from .forms import ProfileUpdateForm, CustomPasswordChangeForm

User = get_user_model()

# ====== views.py ======


class ProfileDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testPass123"
        )
        self.client.login(username="testuser", password="testPass123")
        self.url = reverse("users:detail_profile")

    def test_profile_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/detail_profile.html")
        self.assertEqual(response.context["user"], self.user)


class ProfileUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testPass123", email="old@example.com"
        )
        self.client.login(username="testuser", password="testPass123")
        self.url = reverse("users:update_profile")

    def test_profile_update_valid(self):
        response = self.client.post(
            self.url,
            {"username": "updateduser", "email": "new@example.com"},
            follow=True,
        )
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user.username, "updateduser")
        self.assertEqual(self.user.email, "new@example.com")
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn("Your profile has been updated successfully.", messages)

    def test_profile_update_invalid(self):
        response = self.client.post(self.url, {"username": ""}, follow=True)
        self.assertEqual(response.status_code, 200)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(
            "There was an error updating your profile. Please check the form and try again.",
            messages,
        )


class CustomPasswordChangeViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="oldpassword"
        )
        self.client.login(username="testuser", password="oldpassword")
        self.url = reverse("users:password_change")

    def test_password_change_valid(self):
        response = self.client.post(
            self.url,
            {
                "old_password": "oldpassword",
                "new_password1": "newstrongpassword",
                "new_password2": "newstrongpassword",
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn("Your password has been updated successfully.", messages)

    def test_password_change_invalid(self):
        response = self.client.post(
            self.url,
            {
                "old_password": "wrongpassword",
                "new_password1": "newstrongpassword",
                "new_password2": "newstrongpassword",
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(
            "There was an error updating your password. Please check the form and try again.",
            messages,
        )


class ProfileDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testPass123"
        )
        self.client.login(username="testuser", password="testPass123")
        self.url = reverse("users:delete_profile")

    def test_profile_delete(self):
        response = self.client.post(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username="testuser").exists())
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(
            "Your profile has been deleted successfully. You can continue as a guest or register again!",
            messages,
        )


# ====== urls.py ======


class TestUserURLs(TestCase):
    def test_detail_profile_url_resolves(self):
        url = reverse("users:detail_profile")
        self.assertEqual(resolve(url).func.view_class, ProfileDetailView)

    def test_detail_profile_url_status_code(self):
        response = self.client.get(reverse("users:detail_profile"))
        self.assertIn(response.status_code, [200, 302])

    def test_update_profile_url_resolves(self):
        url = reverse("users:update_profile")
        self.assertEqual(resolve(url).func.view_class, ProfileUpdateView)

    def test_update_profile_url_status_code(self):
        response = self.client.get(reverse("users:update_profile"))
        self.assertIn(response.status_code, [200, 302])

    def test_password_change_url_resolves(self):
        url = reverse("users:password_change")
        self.assertEqual(resolve(url).func.view_class, CustomPasswordChangeView)

    def test_password_change_url_status_code(self):
        response = self.client.get(reverse("users:password_change"))
        self.assertIn(response.status_code, [200, 302])

    def test_delete_profile_url_resolves(self):
        url = reverse("users:delete_profile")
        self.assertEqual(resolve(url).func.view_class, ProfileDeleteView)

    def test_delete_profile_url_status_code(self):
        response = self.client.get(reverse("users:update_profile"))
        self.assertIn(response.status_code, [200, 302])


# ====== forms.py ======


class ProfileUpdateFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword", email="old@example.com"
        )

    def test_valid_form(self):
        form_data = {
            "username": "newusername",
            "email": "new@example.com",
            "first_name": "Test",
            "last_name": "User",
        }
        form = ProfileUpdateForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_missing_username(self):
        form_data = {"email": "new@example.com"}
        form = ProfileUpdateForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)

    def test_invalid_email(self):
        form_data = {"username": "testuser", "email": "invalid-email"}
        form = ProfileUpdateForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)


class CustomPasswordChangeFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="oldpassword"
        )

    def test_valid_password_change(self):
        form_data = {
            "old_password": "oldpassword",
            "new_password1": "newstrongpassword",
            "new_password2": "newstrongpassword",
        }
        form = CustomPasswordChangeForm(user=self.user, data=form_data)
        self.assertTrue(form.is_valid())

    def test_mismatched_passwords(self):
        form_data = {
            "old_password": "oldpassword",
            "new_password1": "newstrongpassword",
            "new_password2": "differentpassword",
        }
        form = CustomPasswordChangeForm(user=self.user, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("new_password2", form.errors)

    def test_incorrect_old_password(self):
        form_data = {
            "old_password": "wrongpassword",
            "new_password1": "newstrongpassword",
            "new_password2": "newstrongpassword",
        }
        form = CustomPasswordChangeForm(user=self.user, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("old_password", form.errors)
