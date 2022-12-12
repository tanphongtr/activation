from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class UserProfile(models.Model):

    project = models.ManyToManyField(
        'app.Project',
        related_name='profiles',
        blank=True,
    )

    photo = models.ImageField(
        _('photo'),
        upload_to='profile/',
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='employee',
    )

    name = models.CharField(
        _('name'),
        max_length=255,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        _('last name'),
        max_length=255,
        null=True,
        blank=True,
    )

    phone = models.CharField(
        _('phone'),
        max_length=255,
        null=True,
        blank=True,
    )

    address = models.CharField(
        _('address'),
        max_length=255,
        null=True,
        blank=True,
    )

    city = models.CharField(
        _('city'),
        max_length=255,
        null=True,
        blank=True,
    )

    state = models.CharField(
        _('state'),
        max_length=255,
        null=True,
        blank=True,
    )

    country = models.CharField(
        _('country'),
        max_length=255,
        null=True,
        blank=True,
    )

    zip_code = models.CharField(
        _('zip code'),
        max_length=255,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        _('created at'),
        auto_now_add=True,
    )

    last_update = models.DateTimeField(
        _('last update'),
        auto_now=True,
    )

    class Meta:
        verbose_name = _('user profile profile')
        verbose_name_plural = _('user profiles')

    def __str__(self):
        return f'{self.user.get_username()} {self.name} {self.last_name}'