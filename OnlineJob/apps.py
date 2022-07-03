from django.apps import AppConfig


class OnlinejobConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'OnlineJob'


    def ready(self):
        import OnlineJob.signals