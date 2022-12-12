from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from app.utils import nanoid_generate, order_id_generate

User = get_user_model()

class Plan(models.Model):
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

    store = models.ManyToManyField(
        to='app.Store',
        related_name='plans',
        blank=True,
    )

    description = models.TextField(
        _('description'),
        blank=True,
    )

    assignee = models.ManyToManyField(
        to=User,
        related_name='assignees',
        blank=True,
    )

    created_by = models.ForeignKey(
        User,
        related_name='plans',
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        _('status'),
        max_length=255,
        default='pending',
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
        verbose_name = _('plan')
        verbose_name_plural = _('plans')
        ordering = ('-created_at',)

    def __str__(self):
        return self.name