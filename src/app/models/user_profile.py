from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class UserProfile(models.Model):

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
        default='',
    )


    first_name = models.CharField(
        _('last name'),
        max_length=255,
        null=True,
        blank=True,
        default='',
    )

    last_name = models.CharField(
        _('last name'),
        max_length=255,
        null=True,
        blank=True,
        default='',
    )

    phone = models.CharField(
        _('phone'),
        max_length=255,
        null=True,
        blank=True,
        default='',
    )

    address = models.CharField(
        _('address'),
        max_length=255,
        null=True,
        blank=True,
        default='',
    )

    city = models.CharField(
        _('city'),
        max_length=255,
        null=True,
        blank=True,
        default='',
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
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')

    def __str__(self):
        return f'{self.user.get_username()}'
