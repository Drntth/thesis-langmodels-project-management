"""
URL configuration for langmodels_project_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path("admin/", admin.site.urls),
    path("", include("home.urls", namespace="home")),
    path("authentication/", include("authentication.urls", namespace="authentication")),
    path("users/", include("users.urls", namespace="users")),
    path(
        "projects/", include("project_management.urls", namespace="project_management")
    ),
    path("ai-docs/", include("ai_documentation.urls", namespace="ai_documentation")),
    path("ai-models/", include("ai_models.urls", namespace="ai_models")),
]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler400 = "home.views.custom_400_view"
handler403 = "home.views.custom_403_view"
handler404 = "home.views.custom_404_view"
handler500 = "home.views.custom_500_view"
