from __future__ import unicode_literals
from django.db import models

class restaurant(models.Model):
    restaurant_id = models.IntegerField(unique=True, primary_key=True)
    restaurant_name = models.CharField(max_length=200)
    cuisines = models.TextField(blank=True, null=True)
    average_cost_for_two = models.IntegerField()
    currency = models.CharField(max_length=120)
    has_table_booking = models.BooleanField()
    has_online_delivery = models.BooleanField()
    aggregate_rating = models.DecimalField(max_digits=2, decimal_places=1)
    rating_color = models.CharField(max_length=50)
    rating_text = models.CharField(max_length=45)
    votes = models.IntegerField()
    country_code = models.IntegerField()
    city = models.CharField(max_length=120)
    address = models.TextField()
    locality = models.TextField()
    locality_verbose = models.TextField()
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.restaurant_name

    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"
