from django.apps import AppConfig


class DriversConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'driver'

    # def ready(self):
    #     from drivers import signals
