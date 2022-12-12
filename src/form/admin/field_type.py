from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from form.models import FieldType
from django.contrib import admin

class FieldTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(FieldType, FieldTypeAdmin)