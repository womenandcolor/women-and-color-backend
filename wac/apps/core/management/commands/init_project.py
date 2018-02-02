# Django
from django.core.management.base import BaseCommand, CommandError

# App
# App
from wac.apps.core.models import Location
from wac.apps.core.management.commands._locations import LOCATIONS


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

    def handle(self, *args, **options):
        self.get_or_create_locations()

        self.stdout.write(self.style.SUCCESS('Successfully initalized the project'))
