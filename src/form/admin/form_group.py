from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from form.models import FormGroup, FormField
from django.contrib import admin
import nested_admin
from django import forms

class FormFieldInline(nested_admin.NestedStackedInline):
    model = FormField
    extra = 0

class FormGroupAdmin(nested_admin.NestedModelAdmin):

    inlines = [
        FormFieldInline,
    ]
    pass




admin.site.register(FormGroup, FormGroupAdmin)