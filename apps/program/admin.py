from django.contrib import admin
from .models import Skill, Program

admin.site.register(Skill)
admin.site.register(Program)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    search_fields = ('name',)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('skills',)
