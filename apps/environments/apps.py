from django.apps import AppConfig

class EnvironmentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.environments'
    verbose_name = "Gestión de Ambientes Academicos"

    def ready(self):

        import apps.environments.signals
