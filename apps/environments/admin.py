from django.contrib import admin
from apps.environments.models.environment import Environment


@admin.register(Environment)
class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')
    search_fields = ('name',)
    ordering = ('name',)
