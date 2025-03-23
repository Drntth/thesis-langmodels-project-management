from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from authentication.views import (
    CustomLoginView,
    CustomRegisterView,
    CustomLogoutView,
    UseAsGuestView,
)
from authentication.forms import CustomLoginForm, CustomRegisterForm

User = get_user_model()

# ====== views.py ======


class CustomLoginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.login_url = reverse("authentication:login")

    def test_login_page_loads(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/login.html")

    def test_login_success(self):
        response = self.client.post(
            self.login_url, {"username": "testuser", "password": "testpassword"}
        )
        self.assertRedirects(response, reverse("home:index"))
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("successfully logged in" in str(msg) for msg in messages))

    def test_login_failure(self):
        response = self.client.post(
            self.login_url, {"username": "testuser", "password": "wrongpassword"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a correct username and password.")

    def test_redirect_authenticated_user(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(self.login_url)
        self.assertRedirects(response, reverse("home:index"))


class CustomRegisterViewTest(TestCase):
    def setUp(self):
        self.register_url = reverse("authentication:register")

    def test_register_page_loads(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/register.html")

    def test_register_weak_password(self):
        response = self.client.post(
            self.register_url,
            {"username": "newuser", "password1": "12345", "password2": "12345"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This password is too short.")

    def test_register_existing_username(self):
        User.objects.create_user(username="newuser", password="SecurePass123!")
        response = self.client.post(
            self.register_url,
            {
                "username": "newuser",
                "password1": "newPassword123",
                "password2": "newPassword123",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A user with that username already exists.")

    def test_register_invalid_form_shows_errors(self):
        response = self.client.post(
            self.register_url,
            {
                "username": "",
                "password1": "newPassword123",
                "password2": "newPassword123",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")


class CustomLogoutViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testuserPass123"
        )
        self.login_url = reverse("authentication:login")
        self.logout_url = reverse("authentication:logout")

    def test_logout_redirects_to_login(self):
        self.client.login(username="testuser", password="testuserPass123")
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, self.login_url)

    def test_logout_message(self):
        self.client.login(username="testuser", password="testuserPass123")
        response = self.client.get(self.logout_url, follow=True)
        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn("You have been logged out.", messages)


class UseAsGuestViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("home:index")

    def test_post_redirects_with_warning_message(self):
        response = self.client.post(reverse("authentication:use_as_guest"))
        self.assertRedirects(response, self.url)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            "You are browsing as a guest. Some features may be unavailable.",
        )
        self.assertEqual(messages[0].level_tag, "warning")


# ====== urls.py ======


class AuthenticationURLsTest(SimpleTestCase):
    def test_login_url_resolves(self):
        url = reverse("authentication:login")
        self.assertEqual(resolve(url).func.view_class, CustomLoginView)

    def test_register_url_resolves(self):
        url = reverse("authentication:register")
        self.assertEqual(resolve(url).func.view_class, CustomRegisterView)

    def test_logout_url_resolves(self):
        url = reverse("authentication:logout")
        self.assertEqual(resolve(url).func.view_class, CustomLogoutView)

    def test_use_as_guest_url_resolves(self):
        url = reverse("authentication:use_as_guest")
        self.assertEqual(resolve(url).func.view_class, UseAsGuestView)

    def test_login_url_status_code(self):
        response = self.client.get(reverse("authentication:login"))
        self.assertIn(response.status_code, [200, 302])

    def test_register_url_status_code(self):
        response = self.client.get(reverse("authentication:register"))
        self.assertIn(response.status_code, [200, 302])

    def test_logout_url_status_code(self):
        response = self.client.get(reverse("authentication:logout"))
        self.assertIn(response.status_code, [200, 302])

    def test_use_as_guest_url_status_code(self):
        response = self.client.get(reverse("authentication:use_as_guest"))
        self.assertIn(response.status_code, [302, 405])


# ====== forms.py ======


class CustomLoginFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="userPass123"
        )

    def test_valid_data(self):
        form = CustomLoginForm(data={"username": "testuser", "password": "userPass123"})
        self.assertTrue(form.is_valid())

    def test_missing_username(self):
        form = CustomLoginForm(data={"username": "", "password": "userPass123"})
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)

    def test_missing_password(self):
        form = CustomLoginForm(data={"username": "testuser", "password": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("password", form.errors)

    def test_field_widget_attributes(self):
        form = CustomLoginForm()

        self.assertEqual(
            form.fields["username"].widget.attrs["class"],
            "form-control border-0 shadow-sm",
        )
        self.assertEqual(
            form.fields["username"].widget.attrs["placeholder"],
            "Enter your username...",
        )
        self.assertEqual(form.fields["username"].widget.attrs["id"], "username")
        self.assertEqual(form.fields["username"].widget.attrs["maxlength"], 150)

        self.assertEqual(
            form.fields["password"].widget.attrs["class"],
            "form-control border-0 shadow-sm",
        )
        self.assertEqual(
            form.fields["password"].widget.attrs["placeholder"],
            "Enter your password...",
        )
        self.assertEqual(form.fields["password"].widget.attrs["id"], "password")
        self.assertEqual(form.fields["password"].widget.attrs["maxlength"], "255")


class CustomRegisterFormTest(TestCase):
    def test_valid_data(self):
        form = CustomRegisterForm(
            data={
                "username": "testuser",
                "email": "test@example.com",
                "first_name": "Test",
                "last_name": "User",
                "password1": "strongpassword123",
                "password2": "strongpassword123",
            }
        )
        self.assertTrue(form.is_valid())

    def test_missing_username(self):
        form = CustomRegisterForm(
            data={
                "username": "",
                "email": "test@example.com",
                "password1": "strongpassword123",
                "password2": "strongpassword123",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)

    def test_missing_email(self):
        form = CustomRegisterForm(
            data={
                "username": "testuser",
                "email": "",
                "password1": "strongpassword123",
                "password2": "strongpassword123",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_passwords_do_not_match(self):
        form = CustomRegisterForm(
            data={
                "username": "testuser",
                "email": "test@example.com",
                "password1": "strongpassword123",
                "password2": "differentpassword",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)

    def test_field_widget_attributes(self):
        form = CustomRegisterForm()

        self.assertEqual(
            form.fields["username"].widget.attrs["class"],
            "form-control border-0 shadow-sm",
        )
        self.assertEqual(
            form.fields["username"].widget.attrs["placeholder"],
            "Enter your username...",
        )
        self.assertEqual(form.fields["username"].widget.attrs["id"], "username")
        self.assertEqual(form.fields["username"].widget.attrs["maxlength"], "150")

        self.assertEqual(
            form.fields["email"].widget.attrs["class"],
            "form-control border-0 shadow-sm",
        )
        self.assertEqual(
            form.fields["email"].widget.attrs["placeholder"],
            "Enter your email address...",
        )
        self.assertEqual(form.fields["email"].widget.attrs["id"], "email")
        self.assertEqual(form.fields["email"].widget.attrs["maxlength"], "254")

        self.assertEqual(
            form.fields["first_name"].widget.attrs["class"],
            "form-control border-0 shadow-sm",
        )
        self.assertEqual(
            form.fields["first_name"].widget.attrs["placeholder"],
            "Enter your first name here...",
        )
        self.assertEqual(form.fields["first_name"].widget.attrs["id"], "first_name")
        self.assertEqual(form.fields["first_name"].widget.attrs["maxlength"], "150")

        self.assertEqual(
            form.fields["last_name"].widget.attrs["class"],
            "form-control border-0 shadow-sm",
        )
        self.assertEqual(
            form.fields["last_name"].widget.attrs["placeholder"],
            "Enter your last name here...",
        )
        self.assertEqual(form.fields["last_name"].widget.attrs["id"], "last_name")
        self.assertEqual(form.fields["last_name"].widget.attrs["maxlength"], "150")

        self.assertEqual(
            form.fields["password1"].widget.attrs["class"],
            "form-control border-0 shadow-sm",
        )
        self.assertEqual(
            form.fields["password1"].widget.attrs["placeholder"],
            "Enter your password...",
        )
        self.assertEqual(form.fields["password1"].widget.attrs["id"], "password")
        self.assertEqual(form.fields["password1"].widget.attrs["maxlength"], "255")

        self.assertEqual(
            form.fields["password2"].widget.attrs["class"],
            "form-control border-0 shadow-sm",
        )
        self.assertEqual(
            form.fields["password2"].widget.attrs["placeholder"],
            "Confirm your password...",
        )
        self.assertEqual(
            form.fields["password2"].widget.attrs["id"], "confirm_password"
        )
        self.assertEqual(form.fields["password2"].widget.attrs["maxlength"], "255")
