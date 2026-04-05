from django.db import models
from django.contrib.auth.models import User

# Profile model to store additional information for each registered user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_image = models.ImageField(upload_to='profile/', null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    
    # Returns the username when the profile object is converted to a string
    def __str__(self):
        return self.user.username