from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import AppUser, GuestUser
from comment.admin import CommentsInline


@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = AppUser
    inlines = [CommentsInline]

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


@admin.register(GuestUser)
class GuestUserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username']
    inlines = [CommentsInline]