from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from app.utils import nanoid_generate

User = get_user_model()


class Location(models.Model):

    code = models.CharField(
        _('code'),
        max_length=255,
        unique=True,
        default=nanoid_generate,
    )
    

    lat = models.FloatField(
        _('latitude'),
    )

    lng = models.FloatField(
        _('longitude'),
    )

    address = models.ForeignKey(
        'place.Address',
        on_delete=models.CASCADE,
        related_name='locations',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.lat} - {self.lng}'

    class Meta:
        verbose_name = _('location')
        verbose_name_plural = _('locations')