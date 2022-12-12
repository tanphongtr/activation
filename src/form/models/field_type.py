from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class FieldType(models.Model):

    icon = models.ImageField(
        _('icon'),
        upload_to='field_type_icons/%Y/%m/%d',
        blank=True,
        null=True,
    )

    name = models.CharField(
        _('name'),
        max_length=255,
    )

    code = models.CharField(
        _('code'),
        max_length=255,
        unique=True,
    )

    description = models.TextField(
        _('description'),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _('field type')
        verbose_name_plural = _('field types')

    def __str__(self):
        return self.name