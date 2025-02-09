from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    def get_default_profile_picture(self):
        if self.profile_picture:
            return self.profile_picture.url
        elif self.user.is_superuser:
            return "/static/images/default_superuser.svg"
        elif self.user.is_staff:
            return "/static/images/default_staff.svg"
        else:
            return "/static/images/default_user.svg"