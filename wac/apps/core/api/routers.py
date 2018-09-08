# App
from wac.apps.core.api.viewsets import LocationViewSet, TopicViewSet, SubscriptionGroupViewSet

# Rest Framework
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'locations', LocationViewSet)
router.register(r'topics', TopicViewSet, base_name="topic")
router.register(r'subscription_groups', SubscriptionGroupViewSet, base_name="subscription_group")
