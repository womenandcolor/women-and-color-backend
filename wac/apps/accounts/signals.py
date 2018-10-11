# Django
from django.dispatch import receiver, Signal
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings

# App
from wac.apps.accounts.models import Profile
from wac.apps.core.models import SubscriptionGroup
from mailchimp3 import MailChimp

import hashlib
import requests

speaker_approved = Signal(providing_args=["profile"])


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=kwargs.get('instance'))


@receiver(post_save, sender=Profile)
def update_email_subscriptions(sender, instance, created, **kwargs):
  if settings.DEBUG==False and not created:
    client = MailChimp(mc_api=settings.MAILCHIMP_API_KEY, timeout=10.0)
    email_hash = hashlib.md5(instance.user.email.lower().encode('utf-8')).hexdigest()
    interests = {}
    subscription_groups = SubscriptionGroup.objects.all();
    for group in subscription_groups:
      interests[group.group_id] = instance.subscription_groups.filter(group_id__iexact=group.group_id).exists()

    client.lists.members.create_or_update(
      list_id=settings.SPEAKER_LIST_ID,
      subscriber_hash=email_hash,
      data={
        'email_address': instance.user.email,
        'status': 'subscribed',
        'status_if_new': 'pending',
        'merge_fields': {
          'FNAME': instance.first_name,
          'LNAME': instance.last_name,
          'IWOMAN': "Yes" if instance.woman else "No",
          'IPOC': "Yes" if instance.poc else "No",
          'ITITLE': instance.position if instance.position else "undisclosed position",
          'ICOMPANY': instance.organization if instance.organization else "undisclosed company",
          'ICITY': instance.location.city if instance.location else "undisclosed location",
        },
        'interests': interests
      }
    )

@receiver(speaker_approved, sender=Profile)
def trigger_frontend_build(sender, **kwargs):
  if settings.DEBUG == False:
    url = "https://api.heroku.com/apps/{}/builds".format(settings.FRONTEND_APP_NAME)
    data = '{"source_blob":{"url":"%s"}}' % settings.FRONTEND_APP_TARBALL # format throws a KeyError
    print(data)
    response = requests.post(
      url,
      data=data,
      headers={
        'Accept': 'application/vnd.heroku+json; version=3',
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(settings.HEROKU_PLATFORM_API_KEY)
      },
    )

    print(response.text)

