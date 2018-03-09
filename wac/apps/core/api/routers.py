# App
from wac.apps.core.api.viewsets import LocationViewSet, TopicViewSet

# Rest Framework
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'locations', LocationViewSet)
router.register(r'topics', TopicViewSet)
