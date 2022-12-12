from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from app.models import Plan
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
        widgets = {
            'assignee': FilteredSelectMultiple('Assignees', False),
        }
class PlanAdmin(admin.ModelAdmin):
    form = PlanForm
    pass

admin.site.register(Plan, PlanAdmin)