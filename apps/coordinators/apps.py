from django.apps import AppConfig

class CoordinatorsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.coordinators"
    verbose_name = "Gestión de Coordinadores"
    def ready(self):
        import apps.coordinators.signals  # noqa
