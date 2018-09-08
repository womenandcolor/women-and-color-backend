# Django
from django.core.management.base import BaseCommand, CommandError

# App
from wac.apps.core.models import Location, SubscriptionGroup
from wac.apps.core.management.commands._locations import LOCATIONS
from wac.apps.core.management.commands._subscription_groups import SUBSCRIPTION_GROUPS


class Command(BaseCommand):
    def get_or_create_locations(self):
        for key, value in LOCATIONS.items():
            for item in value:
                Location.objects.get_or_create(
                    city=item.get('city'),
                    province=item.get('province'),
                    country=key
                )
        self.stdout.write(self.style.SUCCESS('Locations have been created if didn\'t exist'))

    def get_or_create_subscription_groups(self):
        for group in SUBSCRIPTION_GROUPS:
            SubscriptionGroup.objects.get_or_create(
                group_id=group.get('group_id'),
                list_id=group.get('list_id'),
                label=group.get('label')
            )
        self.stdout.write(self.style.SUCCESS('Subscription groups have been created if didn\'t exist'))

    def handle(self, *args, **options):
        self.get_or_create_locations()
        self.get_or_create_subscription_groups()

        self.stdout.write(self.style.SUCCESS('Successfully initalized the project'))
