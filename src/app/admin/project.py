from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from app.models import Project
from django.contrib import admin

class ProjectAdmin(admin.ModelAdmin):

    list_display = ('name', 'campaign_qty', 'store_qty', 'plan_qty', 'created_at',)

    def campaign_qty(self, obj):
        return obj.campaigns.count()
    
    def store_qty(self, obj):
        # return obj.campaigns.all().stores.count()
        qty = 0
        for campaign in obj.campaigns.all():
            qty += campaign.stores.count()
        return qty

    def plan_qty(self, obj):
        qty = 0
        for campaign in obj.campaigns.all():
            stores = campaign.stores.all()
            for store in stores:
                qty += store.plans.count()
        return qty

admin.site.register(Project, ProjectAdmin)