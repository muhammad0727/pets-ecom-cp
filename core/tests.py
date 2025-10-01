from django.test import TestCase, Client

class SmokeTest(TestCase):
    def test_products_api_endpoint_status_code(self):
        """
        Tests that the /api/products/ endpoint returns a 200 status code.
        """
        client = Client()
        response = client.get('/api/products/')
        self.assertEqual(response.status_code, 200)