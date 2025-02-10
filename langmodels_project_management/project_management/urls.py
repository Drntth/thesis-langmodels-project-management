from django.urls import path
from .views import ProjectCreateView, ProjectListView, ProjectDetailView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'projects'

urlpatterns = [
    path('create', ProjectCreateView.as_view(), name='create_project'),
    path('list', ProjectListView.as_view(), name='list_projects'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)