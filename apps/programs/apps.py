from django.apps import AppConfig

class ProgramsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.programs'

    def ready(self):
        import apps.programs.signals.signals
