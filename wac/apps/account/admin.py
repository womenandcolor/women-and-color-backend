from django.contrib import admin

# App
from wac.apps.account.models import (
    Profile
)


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'created_at'
    ]

