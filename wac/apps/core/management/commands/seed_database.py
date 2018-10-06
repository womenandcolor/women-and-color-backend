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
    def create_user(self, woman, poc, job_title, city, topic):
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
        user.profile.position = job_title
        user.profile.organization = fake.company()

        user.profile.poc = poc
        user.profile.woman = woman

        # add location to profile
        location = Location.objects.get(city=city)
        user.profile.location = location

        # add topics to profile
        topic, _created = Topic.objects.get_or_create(topic=topic)
        user.profile.topics.add(topic)

        # set profile status as approved
        user.profile.status = Profile.APPROVED

        user.profile.save()
        self.stdout.write(self.style.SUCCESS('Created or updated user {}'.format(user.profile.first_name)))


    def handle(self, *args, **options):
        self.create_user(True, True, 'Senior Developer', 'Toronto', 'React')
        self.create_user(False, True, 'CEO', 'Waterloo', 'Entrepreneurship')
        self.create_user(True, False, 'Technical Team Lead', 'Vancouver', 'Python')

        self.stdout.write(self.style.SUCCESS('Created some fake profiles for you!'))
