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
from django.urls import include, path
from django.conf.urls import handler400, handler403, handler404, handler500
from home.views import custom_400_view, custom_403_view, custom_404_view, custom_500_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace="home")),
    path('authentication/', include('authentication.urls', namespace="authentication")),
    path('users/', include('users.urls', namespace="users")),
    path('projects/', include('project_management.urls', namespace="project_management")),
    path('ai-docs/', include('ai_documentation.urls',namespace="ai_documentation")),
    path('ai-models/', include('ai_models.urls',namespace="ai_models")),
]

handler400 = "home.views.custom_400_view"
handler403 = "home.views.custom_403_view"
handler404 = "home.views.custom_404_view"
handler500 = "home.views.custom_500_view"