# App
from wac.apps.account.api.viewsets import UserViewSet, ProfileViewSet

# Rest Framework
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'users', UserViewSet, base_name='user')
router.register(r'profiles', ProfileViewSet, base_name='profile')
