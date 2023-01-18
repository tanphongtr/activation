from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class FormGroup(models.Model):
    
    index = models.IntegerField(
        _('index'),
        default=0,
    )

    name = models.CharField(
        _('name'),
        max_length=255,
    )

    form = models.ForeignKey(
        'form_builder.Form',
        related_name='form_groups',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _('form group')
        verbose_name_plural = _('form groups')

    def __str__(self):
        return self.name