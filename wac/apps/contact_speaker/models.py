from django.db import models
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

