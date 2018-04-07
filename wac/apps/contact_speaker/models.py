from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings
from django.template import Context
from django.template.loader import render_to_string, get_template


from wac.apps.accounts.models import Profile


class ContactForm(models.Model):
    code_of_conduct = models.BooleanField(
        default=False
    )

    comments = models.CharField(
        max_length=1000,
        null=True,
        blank=True
    )

    email = models.CharField(
        max_length=250
    )

    event_date = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    event_date = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    event_name = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    event_time = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    full_name = models.CharField(
        max_length=250
    )

    speaker_compensation = models.BooleanField(
        default=False
    )

    venue_name = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )


@receiver(post_save, sender=ContactForm)
def send_message_to_speaker(sender, **kwargs):
    if kwargs.get('created', False):
        contact_form = kwargs.get('instance')
        recipient = contact_form.profile
        subject = 'You have a message from {} via Women and Color'.format(contact_form.full_name)

        context = {
            'recipient_name': recipient.first_name,
            'sender_name': contact_form.full_name,
            'email': contact_form.email,
            'event': contact_form.event_name,
            'date': contact_form.event_date,
            'time': contact_form.event_time,
            'venue': contact_form.venue_name,
            'compensation': ('No', 'Yes')[contact_form.speaker_compensation == True],
            'code_of_conduct': ('No', 'Yes')[contact_form.code_of_conduct == True],
            'comments': contact_form.comments
        }

        txt_message = render_to_string('contact_speaker/email/speaker_contact_form.txt', context)
        html_message = render_to_string('contact_speaker/email/speaker_contact_form.html', context)

        send_mail(subject, txt_message, settings.FROM_EMAIL, [contact_form.profile.user.email], fail_silently=False, html_message=html_message)


@receiver(post_save, sender=ContactForm)
def send_copy_of_message_to_sender_and_wac(sender, **kwargs):
    if kwargs.get('created', False):
        contact_form = kwargs.get('instance')
        recipient = contact_form.profile
        subject = '{} has been sent a message via Women and Color'.format(recipient.first_name)

        context = {
            'recipient_name': recipient.first_name,
            'sender_name': contact_form.full_name,
            'email': contact_form.email,
            'date': contact_form.event_date,
            'time': contact_form.event_time,
            'venue': contact_form.venue_name,
            'compensation': ('No', 'Yes')[contact_form.speaker_compensation == True],
            'code_of_conduct': ('No', 'Yes')[contact_form.code_of_conduct == True],
            'comments': contact_form.comments
        }

        txt_message = render_to_string('contact_speaker/email/speaker_contact_form_copy.txt', context)
        html_message = render_to_string('contact_speaker/email/speaker_contact_form_copy.html', context)

        send_mail(subject, txt_message, settings.FROM_EMAIL, [contact_form.email, settings.MESSAGE_EMAIL], fail_silently=False, html_message=html_message)
