from django.apps import AppConfig

class ContactSpeakerConfig(AppConfig):
    name = 'wac.apps.contact_speaker'

    def ready(self):
        import wac.apps.contact_speaker.signals