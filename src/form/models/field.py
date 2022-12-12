from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Field(models.Model):

    class TypeChoices(models.TextChoices):
        TEXT = 'text', _('Text')
        TEXTAREA = 'textarea', _('Textarea')
        SELECT = 'select', _('Select')
        CHECKBOX = 'checkbox', _('Checkbox')
        RADIO = 'radio', _('Radio')
        FILE = 'file', _('File')
        DATE = 'date', _('Date')
        DATETIME = 'datetime', _('Datetime')
        TIME = 'time', _('Time')
        NUMBER = 'number', _('Number')



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

    type = models.CharField(
        _('type'),
        max_length=255,
        choices=TypeChoices.choices,
        default=TypeChoices.TEXT,
    )

    default_value = models.CharField(
        _('default value'),
        max_length=255,
        blank=True,
        null=True,
    )

    required = models.BooleanField(
        _('required'),
        default=False,
    )

    description = models.TextField(
        _('description'),
        blank=True,
    )

    regex = models.CharField(
        _('regex'),
        max_length=255,
        blank=True,
    )

    form = models.ForeignKey(
        'form.Form',
        related_name='form_fields',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    option = models.ManyToManyField(
        'form.FieldOption',
        related_name='form_fields',
        blank=True,
    )

    min_select = models.IntegerField(
        _('min select'),
        default=0,
    )

    max_select = models.IntegerField(
        _('max select'),
        default=0,
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
        verbose_name = _('field')
        verbose_name_plural = _('fields')
        ordering = ('-created_at',)

    def __str__(self):
        return self.name