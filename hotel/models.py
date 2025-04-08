from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=100, verbose_name="HotelName")
    location = models.CharField(max_length=200, verbose_name="HotelLocation")
    pricePerNight = models.CharField(max_length=20, verbose_name="pricePerNight")

    def __str__(self):
        return self.name