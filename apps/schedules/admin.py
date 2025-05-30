from django.contrib import admin
from apps.schedules.models.schedule import Schedule

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        'program', 'instructor', 'environment', 'day',
        'start_time', 'end_time', 'period'
    )
    list_filter = ('day', 'period', 'environment', 'instructor', 'program')
    search_fields = ('program__name', 'instructor__email', 'environment__name')
    ordering = ('day', 'start_time')
