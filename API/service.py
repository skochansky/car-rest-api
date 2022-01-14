from API.models import Car, CarRating
from collections import Counter


def check_if_car_exist(make, model, data):
    for element in data.json()['Results']:
        if element['Make_Name'].upper() == make.upper():
            if element['Model_Name'].upper() == model.upper():
                car = Car.objects.create(make=make, model=model)
                car.save()
                result = {'success': f'{make} {model} is in the database'}
                return result
    result = {'error': f'{make} {model} is not in the database'}
    return result


def count_ratings():
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


def calculate_avg_rate_for_car(ratings, car_rates_amount):
    for car_id in ratings.keys():
        avg_rating = ratings[car_id] / Counter(car_rates_amount)[car_id]
        car = Car.objects.get(id=car_id)
        car.avg_rating = avg_rating
        car.save()




