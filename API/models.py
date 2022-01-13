from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    avg_rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)


class CarRating(models.Model):
    car_id = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)

