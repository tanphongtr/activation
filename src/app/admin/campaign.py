from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from app.models import Campaign
from django.contrib import admin

class CampaignAdmin(admin.ModelAdmin):
    pass

admin.site.register(Campaign, CampaignAdmin)