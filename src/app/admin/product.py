from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from app.models import Product
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms


class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)