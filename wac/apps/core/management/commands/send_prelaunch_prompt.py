# Django
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse

import csv
import uuid

# App
from wac.apps.accounts.models import Profile
from wac.apps.core.models import Location, Topic


class Command(BaseCommand):
    help = "Email existing users to prompt them to update their accounts before launch. Usage: python manage.py send_prelaunch_prompt"

    def send_email_to_user(self, user):
        subject = 'Please update your speaker profile before we launch our new site!'

        context = {
            'first_name': user.profile.first_name,
            'email': user.email,
            'reset_password_url': reverse('account_reset_password')
        }

        txt_message = render_to_string('core/email/prelaunch_prompt_body.txt', context)
        html_message = render_to_string('core/email/prelaunch_prompt_body.html', context)

        send_mail(subject, txt_message, settings.FROM_EMAIL, [user.email], fail_silently=False, html_message=html_message)


    def handle(self, *args, **options):
        users = User.objects.all();

        for user in users:
            self.send_email_to_user(user)
            self.stdout.write(self.style.SUCCESS('Email sent to {}'.format(user.email)))


