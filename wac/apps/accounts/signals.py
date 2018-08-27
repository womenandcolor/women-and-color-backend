# Django
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings

# App
from wac.apps.accounts.models import Profile
from mailchimp3 import MailChimp

import hashlib


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=kwargs.get('instance'))


@receiver(post_save, sender=Profile)
def update_email_subscriptions(sender, instance, **kwargs):
  client = MailChimp(mc_api=settings.MAILCHIMP_API_KEY)
  email_hash = hashlib.md5(instance.user.email.encode('utf-8')).hexdigest()

  print('email hash!')
  print(email_hash)

  print('instance.newsletter_mailing_list')
  print(instance.newsletter_mailing_list)

  print('instance.speaker_mailing_list')
  print(instance.speaker_mailing_list)

  if instance.newsletter_mailing_list == True:
    client.lists.members.create_or_update(
      list_id=settings.NEWSLETTER_LIST_ID,
      subscriber_hash=email_hash,
      data={
        'email_address': instance.user.email,
        'status': 'subscribed',
        'status_if_new': 'pending',
        'merge_fields': {
          'FNAME': instance.first_name,
          'LNAME': instance.last_name,
        },
      }
    )

  if instance.newsletter_mailing_list == False:
    client.lists.members.update(
      list_id=settings.NEWSLETTER_LIST_ID,
      subscriber_hash=email_hash,
      data={
        'email_address': instance.user.email,
        'status': 'unsubscribed'
      }
    )

  if instance.speaker_mailing_list == True:
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
          'ITITLE': instance.position,
          'ICOMPANY': instance.organization,
          'ICITY': instance.location.city,
        },
      }
    )

  if instance.speaker_mailing_list == False:
    client.lists.members.update(
      list_id=settings.SPEAKER_LIST_ID,
      subscriber_hash=email_hash,
      data={
        'email_address': instance.user.email,
        'status': 'unsubscribed'
      }
    )
