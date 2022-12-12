from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from app.models import Store
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'
        widgets = {
            'campaign': FilteredSelectMultiple('Campaigns', False),
        }

class StoreAdmin(admin.ModelAdmin):
    form = StoreForm
    pass

admin.site.register(Store, StoreAdmin)