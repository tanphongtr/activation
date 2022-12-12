from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from form.models import Form, FormGroup, FormField, Option, FieldType
from django.contrib import admin
import nested_admin
from django import forms

class FormFieldInline(nested_admin.NestedStackedInline):
    model = FormField
    extra = 0


class FormGroupInline(nested_admin.NestedStackedInline):
    model = FormGroup
    extra = 0
    inlines = [
        FormFieldInline,
    ]

class FormAdmin(nested_admin.NestedModelAdmin):
    
    inlines = [
        FormGroupInline,
    ]




admin.site.register(Form, FormAdmin)