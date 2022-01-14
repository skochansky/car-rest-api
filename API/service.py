from API.models import Car, CarRating
from collections import Counter
import json


def check_if_car_exist(make: str, model: str, data: json) -> json:
    make = make.lower()
    model = model.lower()
    for element in data.json()['Results']:
        if element['Make_Name'].lower() == make and element['Model_Name'].lower() == model:
            Car.objects.create(make=make, model=model).save()
            return {'success': f'{make} {model} is in the database'}

    return {'error': f'{make} {model} is not in the database'}


def count_ratings() -> tuple[list[int], dict[int, int]]:
    rates = CarRating.objects.all()
    ratings = {}
    counter_list = []
    for rate in rates:
        if rate.car_id not in ratings:
            ratings[rate.car_id] = rate.rating
            counter_list.append(rate.car_id)
        else:
            ratings[rate.car_id] += rate.rating
            counter_list.append(rate.car_id)

    return counter_list, ratings


def calculate_avg_rate_for_car(ratings: dict[int, int], car_rates_amount: list[int]) -> None:
    for car_id in ratings.keys():
        avg_rating = ratings[car_id] / Counter(car_rates_amount)[car_id]
        car = Car.objects.get(id=car_id)
        car.avg_rating = avg_rating
        car.save()




