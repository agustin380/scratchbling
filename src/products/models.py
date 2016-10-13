from django.db import models
from django.contrib.postgres.fields import ArrayField


class BackScratcher(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    sizes = ArrayField(
        models.CharField(max_length=2)
    )
