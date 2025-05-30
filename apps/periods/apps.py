from django.apps import AppConfig

class PeriodsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.periods'
    verbose_name = "Gestión de Periodos Académicos"

    def ready(self):
        # Importa señales aquí si las usas (en el futuro)
        import apps.periods.signals  # crea el archivo si será usado
