from django.db import models

# Create your models here.
class Interest(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    amount = models.IntegerField()
    piggybank = models.IntegerField(default=0)
    flex = models.IntegerField(default=0)
    flex_dollars = models.IntegerField(default=0)
    safelock = models.IntegerField(default=0)
    investify = models.IntegerField(default=0)