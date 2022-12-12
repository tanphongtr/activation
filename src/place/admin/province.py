from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from place.models import Province, District, Ward, Address
from django.contrib import admin
import nested_admin

class WardInline(nested_admin.NestedStackedInline):
    model = Ward
    extra = 0

class DistrictInline(nested_admin.NestedStackedInline):
    model = District
    extra = 0
    inlines = [
        WardInline,
    ]

class ProvinceAdmin(nested_admin.NestedModelAdmin):
    
    inlines = [
        DistrictInline,
    ]


admin.site.register(Province, ProvinceAdmin)