from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'wac.apps.account'

    def ready(self):
        from wac.apps.account import signals
