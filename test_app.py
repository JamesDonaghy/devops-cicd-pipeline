import unittest
from app import app


class HealthCheckTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health_endpoint_returns_200(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)

    def test_health_endpoint_returns_healthy_status(self):
        response = self.client.get('/health')
        data = response.get_json()
        self.assertEqual(data['status'], 'healthy')

    def test_unknown_route_returns_404(self):
        response = self.client.get('/does-not-exist')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
