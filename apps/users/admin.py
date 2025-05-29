from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.users.models.user import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_coordinator', 'is_teacher')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ()}),
    )

    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)