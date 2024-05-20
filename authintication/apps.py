from django.apps import AppConfig

class CoreConfig(AppConfig):
    name = 'authintication'

    def ready(self):
        import authintication.signals