from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from form.models import FormField
from django.contrib import admin

from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms


class FormFieldForm(forms.ModelForm):
    class Meta:
        model = FormField
        fields = '__all__'
        widgets = {
            'options': FilteredSelectMultiple('Options', False),
        }

class FormFieldAdmin(admin.ModelAdmin):
    form = FormFieldForm

    list_display = (
        'id',
        'name',
        'field_type',

    )

    def field_options(self, obj):
        return ", ".join([p.name for p in obj.field_options.all()])

admin.site.register(FormField, FormFieldAdmin)