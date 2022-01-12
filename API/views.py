from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Car
import json
import requests


@method_decorator(csrf_exempt, name='dispatch')
class CarView(View):

    def get(self, request):
        cars = Car.objects.all()
        cars_serialized_data = []
        for car in cars:
            cars_serialized_data.append({
                'id': car.id,
                'make': car.make,
                'model': car.model,
                'avg_rating': str(car.avg_rating)

            })
        dump = json.dumps(cars_serialized_data)
        return HttpResponse(dump, content_type='application/json', charset='UTF-8')


    def post(self, request):
        post_body = json.loads(request.body)
        make = post_body.get('make')
        model = post_body.get('model')
        car_data = {
            'make': make,
            'model': model
        }
        make = car_data['make']
        response = requests.get(f"https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{make}?format=json")
        for ele in response.json()['Results']:
            print(ele)


        result = {'message': 'This is a POST request'}

        return HttpResponse(json.dumps(result), content_type='application/json', charset='UTF-8')