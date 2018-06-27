from django.contrib.auth.models import User
from django.db import models

# App
from wac.apps.core.models import Location, Topic
from wac.storage_backends import MediaStorage


class Profile(models.Model):
    """
    Extends from the user model
    """
    HE = 'he'
    SHE = 'she'
    THEY = 'they'
    PRONOUNS_CHOICE = (
        (HE, HE),
        (SHE, SHE),
        (THEY, THEY)
    )

    APPROVED = 'approved'
    PENDING = 'pending'
    REJECTED = 'rejected'
    STATUS_OPTIONS = (
        (APPROVED, APPROVED),
        (PENDING, PENDING),
        (REJECTED, REJECTED)
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_OPTIONS,
        default=PENDING
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    topics = models.ManyToManyField(
        Topic
    )

    image = models.CharField(
        max_length=5000,
        default='data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjwhLS0gR2VuZXJhdG9yOiBBZG9iZSBJbGx1c3RyYXRvciAxNi4wLjAsIFNWRyBFeHBvcnQgUGx1Zy1JbiAuIFNWRyBWZXJzaW9uOiA2LjAwIEJ1aWxkIDApICAtLT4NCjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+DQo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4Ig0KCSB3aWR0aD0iMjUwcHgiIGhlaWdodD0iMjUwcHgiIHZpZXdCb3g9Ii05OC41IC05OC41IDI1MCAyNTAiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgLTk4LjUgLTk4LjUgMjUwIDI1MCIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+DQo8cGF0aCBmaWxsPSJub25lIiBkPSJNMCwwaDI0djI0SDBWMHoiLz4NCjxjaXJjbGUgZmlsbD0ibm9uZSIgY3g9IjI2LjUiIGN5PSIyNi41IiByPSIxMjUiLz4NCjxyZWN0IHg9Ii05OC41IiB5PSItOTguNSIgZmlsbD0iI0U1RThGNCIgd2lkdGg9IjI1MCIgaGVpZ2h0PSIyNTAiLz4NCjxwYXRoIGZpbGw9IiMyODNDQTciIGQ9Ik0yOC45NzMsNDkuOTczYzI4LjA0NywwLDUwLjc2NC0yMi43MTcsNTAuNzY0LTUwLjc2NGMwLTI4LjA0Ni0yMi43MTctNTAuNzY0LTUwLjc2NC01MC43NjQNCglTLTIxLjc5MS0yOC44MzctMjEuNzkxLTAuNzkxQy0yMS43OTEsMjcuMjU2LDAuOTI2LDQ5Ljk3MywyOC45NzMsNDkuOTczeiBNMjguOTczLDc1LjM1NGMtMzMuODgzLDAtMTAxLjUyNywxNy4wMDUtMTAxLjUyNyw1MC43NjQNCglWMTUxLjVIMTMwLjV2LTI1LjM4MkMxMzAuNSw5Mi4zNTksNjIuODU1LDc1LjM1NCwyOC45NzMsNzUuMzU0eiIvPg0KPC9zdmc+DQo='
    )

    first_name = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=250,
        null=True,
        blank=True
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
        max_length=1024,
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

    page = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        default='registration'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def display_name(self):
        first_name = self.first_name
        last_name = self.last_name

        if first_name and last_name:
            return u"%s %s".strip() % (first_name, last_name)

        return None

    def __str__(self):
        return self.display_name()

    def __unicode__(self):
        return self.display_name()


class ProfileLocation(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


class ProfileTopic(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    topic = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

class ImageUpload(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    file = models.FileField(blank=False, null=False, storage=MediaStorage())

    created_at = models.DateTimeField(
        auto_now_add=True
    )

class FeaturedTalk(models.Model):
    event_name = models.CharField(
        max_length=250,
        null=False,
        blank=False
    )

    url = models.CharField(
        max_length=250,
        null=False,
        blank=False
    )

    talk_title = models.CharField(
        max_length=250,
        null=False,
        blank=False
    )

    profile = models.ForeignKey(
        Profile,
        related_name='featured_talks',
        on_delete=models.CASCADE,
        null=True
    )

    image = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )

    def __unicode__(self):
        return "{talk_title} at {event_name}".format(
            talk_title=self.talk_title,
            event_name=self.event_name
        )


