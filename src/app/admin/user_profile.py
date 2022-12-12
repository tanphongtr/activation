from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from app.models import UserProfile
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    
    list_display = (
        'user',
        'name',
        'phone',
        'address',
        'city',
    )

admin.site.register(UserProfile, UserProfileAdmin)