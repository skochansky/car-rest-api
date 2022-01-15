from API.models import Car, CarRating
from collections import Counter
import json


def check_if_car_exist(make: str, model: str, data: json) -> json:
    """Check if car exist in external API and if yes, then add it to the
    database"""
    make = make.lower()
    model = model.lower()
    for element in data.json()["Results"]:
        if (
            element["Make_Name"].lower() == make
            and element["Model_Name"].lower() == model
        ):
            Car.objects.create(make=make, model=model).save()
            return {"success": f"{make} {model} is in the database"}

    return {"error": f"{make} {model} is not in the database"}


def count_ratings() -> tuple[list[int], dict[int, int]]:
    """Count the amount of ratings for each car"""
    rates = CarRating.objects.all()
    ratings = {}
    counter_list = []
    for rate in rates:
        if rate.car_id not in ratings:
            ratings[rate.car_id] = rate.rating
        else:
            ratings[rate.car_id] += rate.rating
        counter_list.append(rate.car_id)

    return counter_list, ratings


def calculate_avg_rate_for_car(
    ratings: dict[int, int], car_rates_amount: list[int]
) -> None:
    """Calculate the average rate for each car"""
    for car_id in ratings.keys():
        avg_rating = ratings.get(car_id) / Counter(car_rates_amount).get(car_id)
        try:
            car = Car.objects.get(id=car_id)
            car.avg_rating = avg_rating
            car.save()
        except Car.DoesNotExist:
            pass
