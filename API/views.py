from typing import Iterable

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Car, CarRating
from .service import check_if_car_exist, count_ratings, calculate_avg_rate_for_car
import json
import json5
import requests
from collections import Counter


@method_decorator(csrf_exempt, name='dispatch')
class CarView(View):
    def get(self, request) -> HttpResponse:
        """Fetch all cars from database based on number of reviews.
            available at /popular"""
        counter_list, ratings = count_ratings()
        calculate_avg_rate_for_car(ratings, counter_list)
        cars: Iterable = Car.objects.all()
        cars_serialized_data: list[dict] = []
        for car in cars:
            cars_serialized_data.append({
                'id': car.id,
                'make': car.make,
                'model': car.model,
                'avg_rating': str(car.avg_rating)
            })
        result: json5 = json.dumps(cars_serialized_data)
        return HttpResponse(result, content_type='application/json',
                            charset='UTF-8')

    def post(self, request) -> HttpResponse:
        """Post method for adding new car to database with checking whether
        it exists in the vpic database """
        post_body: json5 = json5.loads(request.body)
        make: str = post_body.get('make')
        model: str = post_body.get('model')
        try:
            request = requests.get(f"https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{make}?format=json")
            print(request.status_code)
            request.raise_for_status()
            result = check_if_car_exist(make, model, request)
        except requests.exceptions.HTTPError as err:
            result = {'error': str(err)}

        return HttpResponse(json.dumps(result), content_type='application/json', charset='UTF-8')


@method_decorator(csrf_exempt, name='dispatch')
class CarDeleteView(View):
    @staticmethod
    def delete(car_id: int) -> HttpResponse:
        try:
            car = Car.objects.get(id=car_id)
            car.delete()
            result = {'messege': 'Car deleted'}
        except Car.DoesNotExist as err:
            result = {'error': str(err)}

        return HttpResponse(json.dumps(result), content_type='application/json', charset='UTF-8')


@method_decorator(csrf_exempt, name='dispatch')
class CarRatingView(View):
    def post(self, request) -> HttpResponse:
        post_body = json5.loads(request.body)
        car_id = post_body.get('car_id')
        rating = post_body.get('rating')
        rate = CarRating.objects.create(car_id=car_id, rating=rating)
        rate.save()
        result = {'message': 'Car rating added'}
        return HttpResponse(json.dumps(result), content_type='application/json',
                            charset='UTF-8')


@method_decorator(csrf_exempt, name='dispatch')
class CarPopularityView(View):
    def get(self) -> HttpResponse:
        """Return top cars based on a number of rates"""
        cars = Car.objects.all()
        cars_serialized_data = []
        ratings = count_ratings()
        ratings = Counter(ratings[0])
        for car in cars:
            if car.id in ratings:
                cars_serialized_data.append({
                    'id': car.id,
                    'make': car.make,
                    'model': car.model,
                    'number_of_rates': ratings[car.id]
                })

            cars_serialized_data = sorted(cars_serialized_data, key=lambda k: k['number_of_rates'], reverse=True)
        result = json.dumps(cars_serialized_data)

        return HttpResponse(result, content_type='application/json',
                            charset='UTF-8')








