
from django.db import models
from datetime import date


# Create your models here.


class Record(models.Model):

    date = models.DateField(default=date.today)
    name = models.CharField(max_length=128)
    tool = models.CharField(max_length=128)
    num = models.IntegerField(default=0)
    skill = models.CharField(max_length=128)
    count = models.IntegerField(default=0)
    publishing = models.BooleanField(default=True)
