from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from place.models import District, Ward
from django.contrib import admin
import nested_admin

class WardInline(nested_admin.NestedStackedInline):
    model = Ward
    extra = 0

class DistrictAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        WardInline,
    ]
admin.site.register(District, DistrictAdmin)