# App
from wac.apps.accounts.api.routers import router

# from django.conf.urls import url, include

app_name="accounts"
urlpatterns = router.urls
