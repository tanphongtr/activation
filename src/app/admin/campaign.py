from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from app.models import Campaign
from django.contrib import admin

class CampaignAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        for field in form.base_fields:
            form.base_fields[field].widget.attrs['autocomplete'] = 'off'
        return form
    autocomplete_fields = []

admin.site.register(Campaign, CampaignAdmin)