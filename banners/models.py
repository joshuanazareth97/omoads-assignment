from django.db import models

class Banner(models.Model):
    name = models.CharField(max_length=200)
