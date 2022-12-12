from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from form.models import Field
from django.contrib import admin

class FieldAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'type',
        'form',
        'field_options',
        'default_value',
    )

    def field_options(self, obj):
        return ", ".join([p.name for p in obj.field_options.all()])

admin.site.register(Field, FieldAdmin)