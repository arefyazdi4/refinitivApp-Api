from django.apps import AppConfig


class EsgApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'esg_api'

    def ready(self):
        import esg_api.signals
