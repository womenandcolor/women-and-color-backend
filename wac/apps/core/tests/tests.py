# Rest Framework
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


# Create your tests here.
class LocationTestCase(APITestCase):
    def setUp(self):
        self.user_endpoint = reverse('core-api:location-list')

    def test_core_endpoint_exists(self):
        self.assertEqual(self.user_endpoint, '/api/v1/locations/')
