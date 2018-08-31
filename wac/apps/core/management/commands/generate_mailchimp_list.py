# Django
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.http import HttpRequest
from django.middleware.csrf import get_token
from allauth.account.views import PasswordResetView
from mailchimp3 import MailChimp
from mailchimp3.mailchimpclient import MailChimpError

# App
from wac.apps.accounts.models import Profile

import hashlib


class Command(BaseCommand):
    help = "Add all users who are not already subscribed to a mailing list. Takes two arguments: 'target_list_id' is the id of the list to subscribe the email to and 'check_list_id' is the id of the list to check if the email is already subscribed."

    def check_if_subscribed(self, profile, list_id, client):
        email_hash = hashlib.md5(profile.user.email.encode('utf-8')).hexdigest()

        subscriber = client.lists.members.get(
            list_id=list_id,
            subscriber_hash=email_hash
        )

        self.stdout.write(self.style.SUCCESS('Email already subscribed to {}: {}'.format(list_id, profile.user.email)))


    def subscribe_to_list(self, profile, list_id, client):
        email_hash = hashlib.md5(profile.user.email.encode('utf-8')).hexdigest()

        data = {
            'email_address': profile.user.email,
            'status': 'subscribed',
            'status_if_new': 'subscribed',
            'merge_fields': {
              'FNAME': profile.first_name,
              'LNAME': profile.last_name,
              'IWOMAN': "Yes" if profile.woman else "No",
              'IPOC': "Yes" if profile.poc else "No",
              'ICITY': profile.location.city if profile.location else "undisclosed location",
            }
        }

        try:
            client.lists.members.create_or_update(
                list_id=list_id,
                subscriber_hash=email_hash,
                data=data
            )
            self.stdout.write(self.style.SUCCESS('Successfully subscribed email {} to list {}'.format(profile.user.email, list_id)))
        except MailChimpError as e:
            self.stdout.write(self.style.WARNING('Unable to add subscriber with email {}'.format(profile.user.email)))
            self.stdout.write(self.style.WARNING('Invalid data: {}'.format(data)))
            self.stdout.write(self.style.WARNING(e))

        except ValueError as e:
            self.stdout.write(self.style.WARNING('Unable to add subscriber with email {}'.format(profile.user.email)))
            self.stdout.write(self.style.WARNING(e))

    # def add_arguments(self, parser):
        # parser.add_argument('target_list_id')
        # parser.add_argument('check_list_id')

    def handle(self, *args, **options):
        profiles = Profile.objects.filter(status=Profile.APPROVED)
        target_list_id = settings.SPEAKER_LIST_ID
        # category_id = settings.CONTACT_PREF_CATEGORY_ID
        # check_list_id = options['check_list_id']
        client = MailChimp(mc_api=settings.MAILCHIMP_API_KEY, timeout=10.0)
        # interests = client.lists.interest_categories.interests.all(list_id=target_list_id, category_id=category_id)
        # print(interests)

        for profile in profiles:
            self.subscribe_to_list(profile, target_list_id, client)



