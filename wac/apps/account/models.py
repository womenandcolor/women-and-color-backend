from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Extends from the user model
    """
    HE = 'HE'
    SHE = 'SHE'
    THEY = 'THEY'
    PRONOUNS_CHOICE = (
        (HE, HE),
        (SHE, SHE),
        (THEY, THEY)
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    woman = models.NullBooleanField(
        null=True,
        blank=True
    )

    poc = models.NullBooleanField(
        null=True,
        blank=True
    )

    pronouns = models.CharField(
        max_length=10,
        choices=PRONOUNS_CHOICE,
        null=True,
        blank=True
    )

    position = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    organization = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    description = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    twitter = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    linkedin = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    website = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def display_name(self):
        return u"%s %s".strip() % (self.user.first_name, self.user.last_name)

    def __str__(self):
        return self.display_name()

    def __unicode__(self):
        return self.display_name()
