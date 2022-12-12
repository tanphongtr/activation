from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class File(models.Model):

    file = models.FileField(upload_to='file/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_by = models.ForeignKey(
        to=User,
        related_name='files',
        on_delete=models.CASCADE,
        to_field='username',
    )

    def __str__(self):
        return self.file.name

    class Meta:
        db_table = 'files'