from django.contrib import admin
from django.contrib.auth import get_user_model, forms
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from app.models import Plan
from django.contrib.admin.widgets import FilteredSelectMultiple


User = get_user_model()

class UserForm(forms.UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'project': FilteredSelectMultiple('Projects', False),
        }
class UserAdmin(UserAdmin):

    form = UserForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Projects'), {'fields': ('project',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, UserAdmin)