from django.db import models


class Car(models.Model):
    DoesNotExist = None
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    avg_rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)