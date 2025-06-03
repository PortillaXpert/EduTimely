from django.contrib import admin
from apps.coordinators.models.coordinator import Coordinator

@admin.register(Coordinator)
class CoordinatorAdmin(admin.ModelAdmin):
    list_display = ("user_full_name", "document_number", "phone", "address")
    search_fields = ("user__first_name", "user__last_name", "document_number", "phone")
    list_filter = ("document_number",)

    def user_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    user_full_name.short_description = "Nombre completo"
