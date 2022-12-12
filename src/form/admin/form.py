from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from form.models import Form, Field
from django.contrib import admin
import nested_admin
from django import forms

class FieldInline(nested_admin.NestedStackedInline):
    model = Field
    extra = 0

class FormAdmin(nested_admin.NestedModelAdmin):
    
    inlines = [
        FieldInline,
    ]




admin.site.register(Form, FormAdmin)