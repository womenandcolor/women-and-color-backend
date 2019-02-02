"""wac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from wac.apps.core.views import StatsView

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^accounts/', include('rest_auth.urls')),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^accounts/registration/', include('rest_auth.registration.urls')),
    re_path(r'^api-token-auth/', obtain_jwt_token),
    re_path(r'^api-verify-token/', verify_jwt_token),


    path(r'api/v1/', include('wac.apps.core.api.urls', namespace='core-api')),
    path(r'api/v1/', include('wac.apps.accounts.api.urls', namespace='account-api')),
    path(r'api/v1/', include('wac.apps.contact_speaker.api.urls', namespace='contact-speaker-api')),
    path(r'api/v1/stats/', StatsView.as_view(), name="stats_view")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

