from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # Add your custom fields to the admin form
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Information", {
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )

    # Show these fields in the user list page
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_superuser")
    search_fields = ("username", "email")
    ordering = ("username",)


admin.site.register(CustomUser, CustomUserAdmin)
