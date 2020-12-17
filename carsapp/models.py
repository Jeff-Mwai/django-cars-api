from django.db import models

# Create your models here.

class Cars(models.Model):
    car_type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    color = models.CharField(max_length=255)
    engine = models.CharField(max_length=100)

    def __str__(self):
        return self.car_type

