# App
from wac.apps.account.api.viewsets import UserViewSet

# Rest Framework
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
