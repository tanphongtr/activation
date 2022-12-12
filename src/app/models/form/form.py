from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Form(models.Model):

    name = models.CharField(
        _('name'),
        max_length=255,
    )

    description = models.TextField(
        _('description'),
        blank=True,
    )

    created_by = models.ForeignKey(
        User,
        related_name='forms',
        on_delete=models.CASCADE,
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
        verbose_name = _('form')
        verbose_name_plural = _('forms')
        ordering = ('-created_at',)

    def __str__(self):
        return self.name