from API.models import Car


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

