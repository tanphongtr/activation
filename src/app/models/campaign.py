from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from app.utils import nanoid_generate, order_id_generate

User = get_user_model()

class Campaign(models.Model):
    name = models.CharField(
        _('name'),
        max_length=255,
    )
    
    code = models.CharField(
        _('code'),
        unique=True,
        default=nanoid_generate,
        max_length=255,
        null=False,
        blank=True,
    )

    description = models.TextField(
        _('description'),
        blank=True,
    )

    project = models.ForeignKey(
        to='app.Project',
        related_name='campaigns',
        on_delete=models.CASCADE,
    )

    created_by = models.ForeignKey(
        User,
        related_name='campaigns',
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
        verbose_name = _('campaign')
        verbose_name_plural = _('campaigns')
        ordering = ('-created_at',)

    def __str__(self):
        return self.name