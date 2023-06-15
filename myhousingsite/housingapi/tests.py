from .models import Resident
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.
class ResidentTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.data = {
            "first_name": "Jon",
            "last_name": "Doe",
            "email": "jon@doe.com",
            "phone": "123-456-7890",
            "birthdate": "1999-01-01",
            "gender": "M"
        }
        self.url = "/api/residents/"

    def test_create_resident(self):
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    