from django.test import TestCase

from .models import Car, CarRating
import requests
import os
import json

os.environ["DJANGO_SETTINGS_MODULE"] = ".car_rest_api.settings"


class TestAPI(TestCase):
    """Test if the API requests are returning 200 OK status code"""

    def setUp(self):
        self.car = Car.objects.create(
            id=1,
            make="Volkswagen",
            model="Golf",
        )

    def test_if_get_cars_api_is_available(self):
        response = requests.get(
            "http://localhost:8000/cars/", headers={"Content-Type": "application/json"}
        )
        self.assertEqual(response.status_code, 200)

    def test_if_post_cars_api_is_available(self):
        data = {"make": "Volkswagen", "model": "Golf"}
        response = requests.post(
            "http://localhost:8000/cars/",
            json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(response.status_code, 200)

    def test_if_post_rate_is_available(self):
        data = {"car_id": 1, "rating": 5}
        response = requests.post(
            "http://localhost:8000/rate/",
            json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(response.status_code, 200)

    def test_if_get_popular_is_available(self):
        response = requests.get(
            "http://localhost:8000/popular/",
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(response.status_code, 200)

    def test_if_delete_cars_api_is_available(self):
        response = requests.delete(
            f"http://localhost:8000/cars/1",
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(response.status_code, 200)
