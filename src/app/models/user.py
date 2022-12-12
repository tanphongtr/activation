from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    project = models.ManyToManyField(
        'app.Project',
        related_name='profiles',
        blank=True,
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

def create_user_profile(sender, instance, created, **kwargs):
    from app.models import UserProfile
    if created:
        UserProfile.objects.create(user=instance)

models.signals.post_save.connect(
    create_user_profile, sender=User, weak=False, dispatch_uid='models.create_user_profile')
