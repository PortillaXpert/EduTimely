from django.contrib import admin
from apps.teachers.models.teacher import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("user", "document_number", "phone", "area")
    search_fields = ("user__username", "document_number", "area")
    list_filter = ("area",)
