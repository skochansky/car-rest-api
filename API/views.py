from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Car
from .service import check_in_car_exist
import json
import requests


@method_decorator(csrf_exempt, name='dispatch')
class CarView(View):
    def get(self):
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
        return HttpResponse(result, content_type='application/json', charset='UTF-8')


    def post(self, request):
        post_body = json.loads(request.body)
        make = post_body.get('make')
        model = post_body.get('model')
        try:
            request = requests.get(f"https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{make}?format=json")
            request.raise_for_status()
            result = check_in_car_exist(make, model, request)
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

