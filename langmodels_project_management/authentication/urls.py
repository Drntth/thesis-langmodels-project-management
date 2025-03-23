from django.urls import path
from .views import CustomLoginView, CustomRegisterView, CustomLogoutView, UseAsGuestView
from django.conf import settings
from django.conf.urls.static import static

app_name = "authentication"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", CustomRegisterView.as_view(), name="register"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("use-as-guest/", UseAsGuestView.as_view(), name="use_as_guest"),
]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
