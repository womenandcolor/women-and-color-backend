from django.conf import settings


def global_settings(request):
    return {
        'FRONTEND_BASE_URL': settings.FRONTEND_BASE_URL
    }