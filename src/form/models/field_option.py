from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class FieldOption(models.Model):

    index = models.IntegerField(
        _('index'),
        default=0,
    )

    name = models.CharField(
        _('name'),
        max_length=255,
    )

    value = models.CharField(
        _('value'),
        max_length=255,
    )

    class Meta:
        verbose_name = _('field option')
        verbose_name_plural = _('field options')

    def __str__(self):
        return self.name + ' - ' + self.value