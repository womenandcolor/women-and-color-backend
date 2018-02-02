from django.contrib import admin

# App
from wac.apps.core.models import (
    Location
)


# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'city',
        'province',
        'country',
        'created_at'
    ]
