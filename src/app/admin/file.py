from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from app.models import File
from django.contrib import admin

class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'created_at', 'upload_by')
    pass
admin.site.register(File, FileAdmin)