from django.urls import path
from .views import ProfileDetailView, ProfileUpdateView, ProfileDeleteView, CustomPasswordChangeView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'

urlpatterns = [
    path("profile/", ProfileDetailView.as_view(), name="detail_profile"),
    path("profile/update", ProfileUpdateView.as_view(), name="update_profile"),
    path('profile/password/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('profile/delete', ProfileDeleteView.as_view(), name='delete_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)