from django.db import models

# Create your models here.
class Location(models.Model):
    city = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    province = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        help_text='Can be province or state'
    )

    country = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __unicode__(self):
        return "{city} city in {province} province/state of {country}".format(
            city=self.city,
            province=self.province,
            country=self.country
        )


class Topic(models.Model):
    topic = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __unicode__(self):
        return self.topic
