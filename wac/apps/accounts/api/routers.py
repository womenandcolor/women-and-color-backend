# App
from wac.apps.accounts.api.viewsets import UserViewSet, ProfileViewSet, ImageUploadViewSet, FeaturedTalkViewSet

# Rest Framework
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'users', UserViewSet, base_name='user')
router.register(r'profiles', ProfileViewSet, base_name='profile')
router.register(r'images', ImageUploadViewSet, base_name='image')
router.register(r'featured_talks', FeaturedTalkViewSet, base_name='featured_talk')