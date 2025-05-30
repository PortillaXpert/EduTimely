from django.contrib import admin
from apps.periods.models.period import Period

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'duration', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active', 'duration')
