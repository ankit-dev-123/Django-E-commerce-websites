from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

# Receiver function that listens for the User model's post_save signal
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # Only creates a Profile object when a new User instance is first created
    if created:
        Profile.objects.create(user=instance)