from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class FieldType(models.Model):
    
    name = models.CharField(
        _('name'),
        max_length=255,
    )

    code = models.CharField(
        _('code'),
        max_length=255,
        unique=True,
    )

    class Meta:
        verbose_name = _('field type')
        verbose_name_plural = _('field types')

    def __str__(self):
        return self.name