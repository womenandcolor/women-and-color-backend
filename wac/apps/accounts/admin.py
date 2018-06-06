from django.contrib import admin

# App
from wac.apps.accounts.models import (
    Profile
)


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'display_name',
        'status',
        'created_at',
        'updated_at'
    ]

