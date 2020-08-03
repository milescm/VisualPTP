from django.db import models
from django.conf import settings


class Csvdata(models.Model):
    objects = models.Manager()
    realtime_timestamp = models.IntegerField()
    utc = models.CharField(max_length=100)
    master_offset = models.IntegerField()
    frequency = models.IntegerField()
    path_delay = models.IntegerField()
