from django.urls import path
from .views import (
    ProjectCreateView,
    ProjectListView,
    ProjectDetailView,
    ProjectUpdateView,
    ProjectDeleteView,
    ProjectMemberCreateView,
    ProjectMemberRemoveView,
)
from django.conf import settings
from django.conf.urls.static import static

app_name = "projects"

urlpatterns = [
    path("create", ProjectCreateView.as_view(), name="create_project"),
    path("list", ProjectListView.as_view(), name="list_projects"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="detail_project"),
    path("<int:pk>/update", ProjectUpdateView.as_view(), name="update_project"),
    path("<int:pk>/delete", ProjectDeleteView.as_view(), name="delete_project"),
    path("<int:pk>/members/add/", ProjectMemberCreateView.as_view(), name="add_member"),
    path(
        "<int:pk>/members/remove/",
        ProjectMemberRemoveView.as_view(),
        name="remove_member",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
