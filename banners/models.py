from django.db import models
from datetime import datetime

class Banner(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class BookingPeriod(models.Model):
    start_date = models.DateField('Booking Start Date')
    end_date = models.DateField('Booking End Date')
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE)

    def __str__(self):
        dates = {
            "start": datetime.strftime(self.start_date,"%d-%b-%Y"),
            "end": datetime.strftime(self.end_date,"%d-%b-%Y"),
        }
        return "{start} to {end}".format(**dates)


class PricePeriod(models.Model):
    start_date = models.DateField('Price Start Date')
    end_date = models.DateField('Price End Date')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE)

    def __str__(self):
        dates = {
            "start": datetime.strftime(self.start_date,"%d-%b-%Y"),
            "end": datetime.strftime(self.end_date,"%d-%b-%Y"),
        }
        return "{start} to {end} @ Rs. {price:.2f}".format(price=self.price,**dates)
