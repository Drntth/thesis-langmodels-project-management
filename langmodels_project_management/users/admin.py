from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')
    search_fields = ('user__username',)
    list_filter = ('user__is_superuser', 'user__is_staff')

    def get_profile_picture(self, obj):
        if obj.profile_picture:
            return obj.profile_picture.url
        return "No picture"
    get_profile_picture.short_description = "Profile picture"
