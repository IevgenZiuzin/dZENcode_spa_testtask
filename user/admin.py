from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import AppUser


class AppUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = AppUser

    list_display = ['pk', 'username']
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )
    fieldsets = UserAdmin.fieldsets + (
        (_('Guest', ), {'fields': ('guest',)}),
    )


admin.site.register(AppUser, AppUserAdmin)
