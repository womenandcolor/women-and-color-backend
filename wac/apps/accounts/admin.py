from django.contrib import admin

# App
from wac.apps.accounts.models import (
    Profile
)
from wac.apps.accounts.signals import speaker_approved


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

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if 'status' in form.changed_data and obj.status == Profile.APPROVED:
            speaker_approved.send(sender=Profile, profile=obj)

