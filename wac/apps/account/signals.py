# Django
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# App
from wac.apps.account.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=kwargs.get('instance'))
