# App
from wac.apps.core.api.viewsets import LocationViewSet

# Rest Framework
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'locations', LocationViewSet)
