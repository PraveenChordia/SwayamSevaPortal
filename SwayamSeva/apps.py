from django.apps import AppConfig


class SwayamsevaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SwayamSeva'

    def ready(self):
        import SwayamSeva.signals  # noqa