from django.db import models
from datetime import datetime


# Create your models here.
class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, max_length=400, default='')
    duration = models.IntegerField(blank=False, )
    upload_time = models.DateTimeField(blank=False, default=datetime.now())


class Podcast(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, max_length=400, default='')
    duration = models.IntegerField(blank=False, )
    upload_time = models.DateTimeField(blank=False, default=datetime.now())
    host = models.CharField(blank=False, max_length=100, default='')
    participants = models.CharField(max_length=600)
