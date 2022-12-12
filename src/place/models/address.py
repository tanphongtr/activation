from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Address(models.Model):

    full_address = models.CharField(
        _('full address'),
        max_length=255,
        null=True,
        blank=True,
    )

    address = models.CharField(
        _('address'),
        max_length=255,
    )

    ward = models.ForeignKey(
        'place.Ward',
        on_delete=models.CASCADE,
        related_name='addresses',
        to_field='code',
    )

    def __str__(self):
        return f'{self.address} - {self.ward} - {self.ward.district} - {self.ward.district.province}'