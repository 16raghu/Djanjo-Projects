from django.db import models

# Stock Data

class Stock (models.Model):
    ticker = models.CharField(max_length=10)
    open = models.FloatField();
    close = models.FloatField()
    volumes = models.IntegerField();


    def __str__(self):
        return  self.ticker