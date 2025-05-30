from django.contrib import admin
from apps.programs.models.programs import Programs

@admin.register(Programs)
class ProgramsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)
