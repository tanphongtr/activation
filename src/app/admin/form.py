from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from app.models import Form, FormField
from django.contrib import admin
import nested_admin

class FormFieldInline(nested_admin.NestedStackedInline):
    model = FormField
    extra = 0

class FormAdmin(nested_admin.NestedModelAdmin):
    
    inlines = [
        FormFieldInline,
    ]


admin.site.register(Form, FormAdmin)