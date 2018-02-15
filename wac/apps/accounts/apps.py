from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'wac.apps.accounts'

    def ready(self):
        from wac.apps.accounts import signals
