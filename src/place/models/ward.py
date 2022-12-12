from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Ward(models.Model):
    
    name = models.CharField(
        _('name'),
        max_length=255,
    )

    code = models.CharField(
        _('code'),
        unique=True,
        max_length=255,
        null=False,
        blank=True,
    )

    district = models.ForeignKey(
        'place.District',
        on_delete=models.CASCADE,
        related_name='wards',
        to_field='code',
    )

    def __str__(self):
        return self.name