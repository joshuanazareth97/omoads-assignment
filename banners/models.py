from django.db import models

class Banner(models.Model):
    name = models.CharField(max_length=200)

class BookingPeriod(models.Model):
    start_date = models.DateTimeField('Booking Start Date')
    end_date = models.DateTimeField('Booking End Date')
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE)

class PricePeriod(models.Model):
    start_date = models.DateTimeField('Booking Start Date')
    end_date = models.DateTimeField('Booking End Date')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE)
