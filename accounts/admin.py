from django.contrib import admin
from .models import CustomUser
from django.utils.html import format_html


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        "display_username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "is_verified",
    ]

    def display_username(self, instance):
        return format_html(f"<b style='color:orange'>{instance.username}</b>")

    display_username.short_description = "username"

    fieldsets = [
        (
            "General Information",
            {"fields": ["first_name", "last_name", "username", "is_active"]},
        ),
        ("Crediential", {"fields": ["email", "password"], "classes": ["wide"]}),
        (
            "Admin Info",
            {"fields": ["is_superuser", "is_staff"], "classes": ["collapse"]},
        ),
        (
            "Verification",
            {"fields": ["is_verified", "verification_token"], "classes": ["collapse"]},
        ),
        ("Date", {"fields": ["last_login"], "classes": ["collapse"]}),
        ("Groups", {"fields": ["groups"], "classes": ["collapse"]}),
        (
            "Permissions",
            {"fields": ["user_permissions"], "classes": ["collapse"]},
        ),
    ]


admin.site.register(CustomUser, CustomUserAdmin)
