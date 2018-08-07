from django.contrib import admin

# App
from wac.apps.contact_speaker.models import (
    ContactForm
)

# Register your models here.
@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'email',
        'event_date',
        'event_name',
        'profile',
        'comments',
        'created_at',
    ]

