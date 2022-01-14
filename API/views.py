from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Car, CarRating
from .service import check_if_car_exist, count_ratings, calculate_avg_rate_for_car
import json
import requests
from collections import Counter


@method_decorator(csrf_exempt, name='dispatch')
class CarView(View):
    def get(self, request):
        counter_list, ratings = count_ratings()
        calculate_avg_rate_for_car(ratings, counter_list)
        cars = Car.objects.all()
        cars_serialized_data = []
        for car in cars:
            cars_serialized_data.append({
                'id': car.id,
                'make': car.make,
                'model': car.model,
                'avg_rating': str(car.avg_rating)
            })
            result = json.dumps(cars_serialized_data)
        return HttpResponse(result, content_type='application/json',
                            charset='UTF-8')

    def post(self, request):
        post_body = json.loads(request.body)
        make = post_body.get('make')
        model = post_body.get('model')
        try:
            request = requests.get(f"https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{make}?format=json")
            request.raise_for_status()
            result = check_if_car_exist(make, model, request)
        except requests.exceptions.HTTPError as err:
            result = {'error': str(err)}

        return HttpResponse(json.dumps(result), content_type='application/json', charset='UTF-8')


@method_decorator(csrf_exempt, name='dispatch')
class CarDeleteView(View):
    def delete(self, request, car_id):
        try:
            car = Car.objects.get(id=car_id)
            car.delete()
            result = {'messege': 'Car deleted'}
        except Car.DoesNotExist as err:
            result = {'error': str(err)}

        return HttpResponse(json.dumps(result), content_type='application/json', charset='UTF-8')


@method_decorator(csrf_exempt, name='dispatch')
class CarRatingView(View):
    def post(self, request):
        post_body = json.loads(request.body)
        car_id = post_body.get('car_id')
        rating = post_body.get('rating')
        rate = CarRating.objects.create(car_id=car_id, rating=rating)
        rate.save()
        result = {'message': 'Car rating added'}
        return HttpResponse(json.dumps(result), content_type='application/json',
                            charset='UTF-8')


@method_decorator(csrf_exempt, name='dispatch')
class CarPopularityView(View):
    def get(self, request):
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








