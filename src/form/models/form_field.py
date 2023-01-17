from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class FormField(models.Model):

    index = models.IntegerField(
        _('index'),
        default=0,
    )

    name = models.CharField(
        _('name'),
        max_length=255,
    )

    label = models.CharField(
        _('label'),
        max_length=255,
        null=True,
        blank=True,
    )

    field_type = models.ForeignKey(
        'form.FieldType',
        related_name='form_fields',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    default_value = models.CharField(
        _('default value'),
        max_length=255,
        blank=True,
        null=True,
    )

    use_default = models.BooleanField(
        _('use default'),
        default=False,
    )

    required = models.BooleanField(
        _('required'),
        default=False,
    )

    # ForeignKey to FormGroup
    form_group = models.ForeignKey(
        'form.FormGroup',
        related_name='form_fields',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    options = models.ManyToManyField(
        'form.FieldOption',
        related_name='form_fields',
        blank=True,
    )

    class Meta:
        verbose_name = _('form field')
        verbose_name_plural = _('form fields')
        # ordering = ('-created_at',)

    def __str__(self):
        return self.name