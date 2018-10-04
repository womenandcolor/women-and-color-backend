# Django
from django.core.management.base import BaseCommand, CommandError

# App
from wac.apps.core.models import Location, Topic, SubscriptionGroup
from wac.apps.accounts.models import Profile
from django.contrib.auth.models import User

from wac.apps.core.management.commands._locations import LOCATIONS
from wac.apps.core.management.commands._subscription_groups import SUBSCRIPTION_GROUPS

from faker import Faker, Factory
from faker.providers import internet
from faker.providers import company
import uuid

class Command(BaseCommand):
    def create_user(self):
        fake = Factory.create()
        fake.add_provider(internet)
        fake.add_provider(company)
        email = fake.email()
        user = User.objects.create_user(
            email,
            email,
            uuid.uuid4()
        )
        user.save()

        name = fake.name()

        user.profile.first_name = name.split(' ')[0]
        user.profile.last_name = name.split(' ')[1]
        user.profile.position = 'Senior Developer'
        user.profile.organization = fake.company()

        user.profile.poc = True
        user.profile.woman = True

        # add location to profile
        location = Location.objects.get(city='Toronto')
        user.profile.location = location

        # add topics to profile
        topic, _created = Topic.objects.get_or_create(topic='React')
        user.profile.topics.add(topic)

        # set profile status as approved
        user.profile.status = Profile.APPROVED

        user.profile.save()
        self.stdout.write(self.style.SUCCESS('Created or updated user {}'.format(user.profile.first_name)))


    def handle(self, *args, **options):
        self.create_user()

        self.stdout.write(self.style.SUCCESS('Created a fake profile for you!'))
