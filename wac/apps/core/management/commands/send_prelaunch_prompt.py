# Django
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.http import HttpRequest
from django.middleware.csrf import get_token
from allauth.account.views import PasswordResetView

# App
from wac.apps.accounts.models import Profile
from wac.apps.core.models import Location, Topic


class Command(BaseCommand):
    help = "Email existing users to prompt them to update their accounts before launch. Accepts one argument, either 'all' to send to all users or an email address to send to one user."

    def send_email_to_user(self, user):
        request = HttpRequest()
        request.method = 'POST'

        if settings.DEBUG:
            request.META['HTTP_HOST'] = 'localhost:8000'
        else:
            request.META['HTTP_HOST'] = 'www.womenandcolor.com'

        request.POST = {
            'email': user.email,
            'csrfmiddlewaretoken': get_token(HttpRequest())
        }

        PasswordResetView.as_view()(request)

    def add_arguments(self, parser):
        parser.add_argument('user')

    def handle(self, *args, **options):
        recipient = options['user']

        if recipient == 'all':
            users = User.objects.all();
        else:
            users = User.objects.filter(email=recipient)

        self.stdout.write(self.style.SUCCESS('Sending password reset emails to {} users'.format(users.count())))

        for user in users:
            self.send_email_to_user(user)
            self.stdout.write(self.style.SUCCESS('Email sent to {}'.format(user.email)))


