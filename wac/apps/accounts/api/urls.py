# App
from wac.apps.accounts.api.routers import router

# from django.conf.urls import url, include

app_name="accounts"
urlpatterns = router.urls

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
