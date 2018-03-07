from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings

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
        subject = 'You have a message from Women and Color'
        contact_form = kwargs.get('instance')
        recipient = contact_form.profile

        message = ("""
        Hi {recipient_name},

        {sender_name} has sent you a message from www.womenandcolor.com!

        From: {email}
        Event date: {date}
        Event time: {time}
        Venue: {venue}
        Speaker compensation: {compensation}
        Message: "{comments}"

        If you're interested in this speaking opportunity, please contact {sender_name} at {email}.
        """).format(
            recipient_name=recipient.first_name,
            sender_name=contact_form.full_name,
            email=contact_form.email,
            date=contact_form.event_date,
            time=contact_form.event_time,
            venue=contact_form.venue_name,
            compensation=contact_form.speaker_compensation,
            comments=contact_form.comments
        )

        send_mail(subject, message, settings.FROM_EMAIL, [contact_form.profile.user.email], fail_silently=False)
